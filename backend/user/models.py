import ormar
import strawberry
from db import MainMeta


class User(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: str = ormar.String(primary_key=True, max_length=255)
    username: str = ormar.String(max_length=255, nullable=False, unique=True)
    password: str = ormar.String(max_length=255, nullable=False)
    firstname: str = ormar.String(max_length=255)
    address: str = ormar.String(max_length=1024)
    is_superuser: bool = ormar.Boolean(nullable=False)


@strawberry.type
class GraphQLUser():
    id_: str
    username: str
    password: str
    firstname: str
    address: str
    is_superuser: bool


@strawberry.input
class GraphQLUserUpdateInput():
    address: str
    firstname: str
    is_superuser: bool
