from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


class CreateUser(BaseModel):
    username: str
    password: str
    firstname: str
    address: Optional[str] = ""
    is_superuser: Optional[bool] = False


class GetUser(CreateUser):
    id_: str


# class UserUpdate(models.CreateUpdateDictModel):
#     password: Optional[str]
#     email: Optional[str]
#     first_name: Optional[str]
#     address: Optional[str]
#     is_active: Optional[bool]
#     is_superuser: Optional[bool]
#     is_verified: Optional[bool]

# class UserDB(User):
#     hashed_password: str

#     class Config:
#         orm_mode = True
