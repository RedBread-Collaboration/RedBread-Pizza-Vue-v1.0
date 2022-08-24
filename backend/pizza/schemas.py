from pydantic import BaseModel


class CreatePizza(BaseModel):
    name: str
    ingredients: str
    photo: str
    price_small: int
    price_medium: int
    price_large: int


class GetPizza(CreatePizza):
    id_: str
