import json
from typing import List

import strawberry
from cart.models import Cart
from db import get_uuid
from fastapi_jwt_auth import AuthJWT
from pizza.models import PizzaTemplate
from starlette.requests import Request
from strawberry.types import Info
from user.models import User

from .models import GraphQLTicket, GraphQLTicketInput, Ticket, TicketStatus
from .schemas import CreateTicket


@strawberry.type
class TicketQuery():

    @strawberry.field
    async def ticket(self, info: Info) -> List[GraphQLTicket]:
        return await Ticket.objects.all()


@strawberry.type
class TicketMutation:

    @strawberry.field
    async def ticket(self, ticket: GraphQLTicketInput, info: Info) -> GraphQLTicket:
        result = []
        request: Request = info.context["request"]
        session_id: str = request.headers.get("Session_ID")

        if not session_id:
            raise Exception("No session_id in headers")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        current_user = await User.objects.get_or_none(username=username)

        address = ticket.address

        if not address and current_user:
            address = current_user.dict()["address"]
        elif address:
            if current_user:
                await User.objects.filter(username=username).update(address=address)
        else:
            raise Exception("No address")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        # current_user = await User.objects.get_or_none(username=username)

        if username:
            carts = await Cart.objects.all(username=username)
        else:
            carts = await Cart.objects.all(session_id=session_id)

        final_price = 0
        if not carts:
            raise Exception("User have no carts")

        for cart in carts:
            cart = cart.dict()

            pizza = await PizzaTemplate.objects.get(id_=cart["product_id"])
            pizza = pizza.dict()

            pizza_name = pizza["name"]
            pizza_dough = cart["dough"]
            pizza_count = cart["count"]
            pizza_size = cart["size"]
            pizza_pieces = cart["pieces"]
            pizza_additives = cart["additives"]
            price = cart["final_price"]
            final_price += price

            msg = {
                "pizza_name": pizza_name,
                "pizza_count": pizza_count,
                "pizza_dough": pizza_dough,
                "pizza_size": pizza_size,
                "pizza_pieces": pizza_pieces,
                "pizza_additives": pizza_additives,
                "price": price,
            }

            # msg = f"{pizza_name} x{pizza_count} ({pizza_dough},
            # тесто, {pizza_size}, {pizza_pieces}, начинка: {pizza_additives}) - {price};"
            result.append(msg)

        items = json.dumps(result)

        ticket = CreateTicket(items=items,
                              status=TicketStatus.in_progress.value,
                              address=address,
                              username=username,
                              session_id=session_id,
                              final_price=final_price)

        for cart in carts:
            cart = cart.dict()
            await Cart.objects.delete(id_=cart["id_"])

        return await Ticket.objects.create(id_=get_uuid(), **ticket.dict())
