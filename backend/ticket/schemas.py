from enum import Enum

from pydantic import BaseModel
from typing import Optional


class TicketStatus(str, Enum):
    in_progress = "В процессе"
    frozen = "Заморожен"
    finished = "Завершён"


class CreateTicket(BaseModel):
    items: str
    status: TicketStatus
    address: str
    username: Optional[str]
    session_id: str
    final_price: int


class GetTicket(CreateTicket):
    id_: str
