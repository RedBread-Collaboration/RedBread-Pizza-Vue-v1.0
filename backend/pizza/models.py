import ormar
import strawberry
from db import MainMeta


class PizzaTemplate(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: str = ormar.String(primary_key=True, max_length=255)
    name: str = ormar.String(max_length=255, unique=True)
    ingredients: str = ormar.String(max_length=1024)
    photo: str = ormar.String(max_length=1024)
    price_small: int = ormar.Integer(minimum=0)
    price_medium: int = ormar.Integer(minimum=0)
    price_large: int = ormar.Integer(minimum=0)


@strawberry.type
class GraphQLPizza():
    id_: str
    name: str
    ingredients: str
    photo: str
    price_small: int
    price_medium: int
    price_large: int
