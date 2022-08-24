from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PizzaSize(str, Enum):
    small = "Маленькая (25 см.)"
    medium = "Средняя (30 см.)"
    large = "Большая (35 см.)"


class PizzaDough(str, Enum):
    traditional = "Традиционное"
    thin = "Тонкое"


class PizzaPiece(str, Enum):
    one = "Целая"
    four = "4 куска"
    six = "6 кусков"
    eight = "8 кусков"


class CreateCartItem(BaseModel):
    product_id: str
    username: Optional[str]
    session_id: str
    count: int
    dough: PizzaDough
    size: PizzaSize
    pieces: PizzaPiece
    additives: Optional[str]
    final_price: int


class GetCartItem(CreateCartItem):
    id_: str
