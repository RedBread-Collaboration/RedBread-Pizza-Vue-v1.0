import ormar
import strawberry
from db import MainMeta
from enum import Enum
from typing import Optional


class Ticket(ormar.Model):

    class Meta(MainMeta):
        pass

    id_: str = ormar.String(primary_key=True, max_length=255)
    items: str = ormar.String(max_length=4096)
    status: str = ormar.String(max_length=255)
    address: str = ormar.String(max_length=255)
    username: str = ormar.String(max_length=255, nullable=True)
    session_id: str = ormar.String(max_length=255)
    final_price: int = ormar.Integer(minimum=0)


@strawberry.enum
class TicketStatus(Enum):
    in_progress = "В процессе"
    frozen = "Заморожён"
    finished = "Завершён"


@strawberry.type
class GraphQLTicket():
    id_: str
    items: str
    status: str
    address: str
    username: Optional[str]
    session_id: str
    final_price: int


@strawberry.input
class GraphQLTicketInput():
    address: Optional[str]
