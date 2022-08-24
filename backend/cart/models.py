from enum import Enum

import ormar
import strawberry
from db import MainMeta
from pizza.models import GraphQLPizza
from typing import Optional


class Cart(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: str = ormar.String(primary_key=True, max_length=255)
    product_id: str = ormar.String(max_length=255)
    username: str = ormar.String(max_length=255, nullable=True)
    session_id: str = ormar.String(max_length=255)
    count: int = ormar.Integer(minimum=1)
    dough: str = ormar.String(max_length=255)
    size: str = ormar.String(max_length=255)
    pieces: str = ormar.String(max_length=255)
    additives: str = ormar.String(max_length=255, nullable=True)
    final_price: int = ormar.Integer(minimum=0)


@strawberry.enum
class PizzaSize(Enum):
    small = "Маленькая (25 см.)"
    medium = "Средняя (30 см.)"
    large = "Большая (35 см.)"


@strawberry.enum
class PizzaDough(Enum):
    traditional = "Традиционное"
    thin = "Тонкое"


@strawberry.enum
class PizzaPiece(Enum):
    one = "Целая"
    four = "4 куска"
    six = "6 кусков"
    eight = "8 кусков"


@strawberry.type
class GraphQLCart():
    id_: str
    product_id: str
    username: Optional[str]
    session_id: str
    count: int
    dough: str
    size: str
    pieces: int
    additives: Optional[str]
    final_price: int
    product: GraphQLPizza


@strawberry.input
class GraphQLCartInput():
    product_id: str
    count: int
    dough: PizzaDough
    size: PizzaSize
    pieces: PizzaPiece
    additives: Optional[str]


@strawberry.input
class GraphQLCartUpdateCountInput():
    id_: str
    count: int
