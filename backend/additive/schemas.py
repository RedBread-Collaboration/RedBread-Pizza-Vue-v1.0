from pydantic import BaseModel


class CreateAdditive(BaseModel):
    name: str
    photo: str
    price: int


class GetAdditive(CreateAdditive):
    id_: str
