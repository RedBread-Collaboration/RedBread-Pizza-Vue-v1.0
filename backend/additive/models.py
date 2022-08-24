import ormar
import strawberry
from db import MainMeta


class Additive(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: str = ormar.String(primary_key=True, max_length=255)
    name: str = ormar.String(max_length=255, unique=True)
    photo: str = ormar.String(max_length=1024)
    price: int = ormar.Integer(minimum=0)


@strawberry.type
class GraphQLAdditive():
    id_: str
    name: str
    photo: str
    price: int
