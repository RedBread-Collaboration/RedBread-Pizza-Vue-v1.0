from typing import List

import strawberry
from db import get_uuid
from fastapi_jwt_auth import AuthJWT
from starlette.requests import Request
from strawberry.types import Info

from .models import GraphQLUser, User, GraphQLUserUpdateInput
from .schemas import Settings


@AuthJWT.load_config
def get_config():
    return Settings()


@strawberry.type
class UserQuery:

    @strawberry.field
    async def user(self) -> List[GraphQLUser]:
        return await User.objects.all()

    @strawberry.field
    async def whoami(self, info: Info) -> GraphQLUser:
        request: Request = info.context["request"]

        authorize = AuthJWT(req=request)
        current_user = authorize.get_jwt_subject()
        print(current_user)
        user = await User.objects.get_or_none(username=current_user)
        return GraphQLUser(**user.dict())


@strawberry.type
class UserMutation:

    @strawberry.field
    async def login(self, username: str, password: str, info: Info) -> str:

        user = await User.objects.get_or_none(username=username)

        if user:
            request: Request = info.context["request"]
            authorize = AuthJWT(req=request)

            return authorize.create_access_token(subject=username, expires_time=86400)

        return "User not found"

    @strawberry.field
    async def register(self,
                       username: str,
                       password: str,
                       firstname: str,
                       info: Info,
                       address: str = "") -> GraphQLUser:
        return await User.objects.create(id_=get_uuid(),
                                         username=username,
                                         password=password,
                                         firstname=firstname,
                                         address=address,
                                         is_superuser=False)

    @strawberry.field
    async def update_user(self, user: GraphQLUserUpdateInput, info: Info) -> GraphQLUser:
        request: Request = info.context["request"]
        session_id: str = request.headers.get("Session_ID")

        if not session_id:
            raise Exception("No session_id in headers")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        current_user = await User.objects.get_or_none(username=username)

        if not current_user:
            raise Exception("No user in db")

        await current_user.update(firstname=user.firstname, address=user.address, is_superuser=user.is_superuser)

        return await User.objects.get(id_=current_user.dict()["id_"])
