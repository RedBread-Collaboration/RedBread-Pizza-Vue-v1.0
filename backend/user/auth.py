from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend, CookieTransport, JWTStrategy)

from .models import get_user_db
from .schemas import User, UserCreate, UserDB, UserUpdate

SECRET = "SECRET"


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport(cookie_max_age=3600, cookie_secure=False)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = Depends(fastapi_users.current_user(active=True))
current_active_user1 = fastapi_users.current_user(active=True)
current_superuser_user = Depends(fastapi_users.current_user(active=True, superuser=True))
