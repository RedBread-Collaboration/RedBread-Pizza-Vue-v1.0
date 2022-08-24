from typing import List, Optional
from warnings import catch_warnings

import strawberry
from additive.models import Additive
from db import get_uuid
from fastapi_jwt_auth import AuthJWT
from pizza.models import PizzaTemplate
from starlette.requests import Request
from strawberry.types import Info
from user.models import User

from .models import (Cart, GraphQLCart, GraphQLCartInput, GraphQLCartUpdateCountInput, PizzaSize)
from .schemas import CreateCartItem


@strawberry.type
class CartQuery:

    @strawberry.field
    async def cart(self, info: Info) -> List[GraphQLCart]:
        result = []
        request: Request = info.context["request"]
        session_id: Optional[str] = request.headers.get("Session_ID")

        authorize = AuthJWT(req=request)
        current_user = authorize.get_jwt_subject()
        current_user = await User.objects.get_or_none(username=current_user)

        if current_user:
            await Cart.objects.filter(username=current_user.dict()["username"]).update(session_id=session_id)
            user_carts = await Cart.objects.all(username=current_user.dict()["username"])
        elif session_id:
            user_carts = await Cart.objects.all(session_id=session_id)
        else:
            user_carts = []

        for cart in user_carts:
            cart = cart.dict()
            product = await PizzaTemplate.objects.get_or_none(pk=cart["product_id"])
            result.append(GraphQLCart(**cart, product=product))
        return result


@strawberry.type
class CartMutation:

    @strawberry.field
    async def cart(self, cart: GraphQLCartInput, info: Info) -> GraphQLCart:
        request: Request = info.context["request"]
        session_id: str = request.headers.get("Session_ID")

        if not session_id:
            raise Exception("No session_id in headers")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        # current_user = await User.objects.get_or_none(username=username)

        pizza = await PizzaTemplate.objects.get_or_none(id_=cart.product_id)

        if not pizza:
            raise Exception("Invalid product_id")

        pizza = pizza.dict()

        size = cart.size

        if size == PizzaSize.small:
            price = pizza["price_small"]
        elif size == PizzaSize.medium:
            price = pizza["price_medium"]
        else:
            price = pizza["price_large"]

        price *= cart.count

        if cart.additives:
            additives = str(cart.additives).split(", ")
        else:
            additives = ""

        for additive in additives:
            db_additive = await Additive.objects.get_or_none(name=additive)

            if not db_additive:
                raise Exception(f"Invalid additive: {additive}")

            price += db_additive.dict()["price"]

        new_cart = CreateCartItem(product_id=cart.product_id,
                                username=username,
                                session_id=session_id,
                                count=cart.count,
                                dough=cart.dough.value,
                                size=cart.size.value,
                                pieces=cart.pieces.value,
                                additives=cart.additives,
                                final_price=price)

        return await Cart.objects.create(id_=get_uuid(), **new_cart.dict())

    @strawberry.field
    async def delete_cart(self, id_: str, info: Info) -> None:
        request: Request = info.context["request"]
        session_id: str = request.headers.get("Session_ID")

        if not session_id:
            raise Exception("No session_id in headers")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        # current_user = await User.objects.get_or_none(username=username)

        old_cart = await Cart.objects.get_or_none(id_=id_)

        if not old_cart:
            raise Exception("Invalid cart_id")

        old_cart = old_cart.dict()

        if old_cart["username"] != username:
            raise Exception("Invalid username")

        await Cart.objects.delete(id_=id_)

    @strawberry.field
    async def cart_update_count(self, cart: GraphQLCartUpdateCountInput, info: Info) -> GraphQLCart:
        request: Request = info.context["request"]
        session_id: str = request.headers.get("Session_ID")

        if not session_id:
            raise Exception("No session_id in headers")

        authorize = AuthJWT(req=request)
        username = authorize.get_jwt_subject()
        # current_user = await User.objects.get_or_none(username=username)

        old_cart = await Cart.objects.get_or_none(id_=cart.id_)

        if not old_cart:
            raise Exception("Invalid cart_id")

        old_cart = old_cart.dict()

        if old_cart["username"] != username:
            raise Exception("Invalid username")

        pizza = await PizzaTemplate.objects.get_or_none(id_=old_cart["product_id"])

        if not pizza:
            raise Exception("Invalid product_id")

        pizza = pizza.dict()

        size = old_cart["size"]

        if size == PizzaSize.small:
            price = pizza["price_small"]
        elif size == PizzaSize.medium:
            price = pizza["price_medium"]
        else:
            price = pizza["price_large"]

        price *= cart.count

        if old_cart["additives"]:
            additives = str(old_cart["additives"]).split(", ")
        else:
            additives = ""

        for additive in additives:
            db_additive = await Additive.objects.get_or_none(name=additive)

            if not db_additive:
                raise Exception(f"Invalid additive: {additive}")

            price += db_additive.dict()["price"]
        await Cart.objects.filter(id_=cart.id_).update(count=cart.count, final_price=price)
        return await Cart.objects.get(id_=cart.id_)

    @strawberry.field
    async def calculate_price(self, cart: GraphQLCartInput, info: Info) -> int:
        pizza = await PizzaTemplate.objects.get_or_none(id_=cart.product_id)

        if not pizza:
            raise Exception("Invalid product_id")

        pizza = pizza.dict()

        size = cart.size

        if size == PizzaSize.small:
            price = pizza["price_small"]
        elif size == PizzaSize.medium:
            price = pizza["price_medium"]
        else:
            price = pizza["price_large"]

        price *= cart.count

        if cart.additives:
            additives = str(cart.additives).split(", ")
        else:
            additives = ""

        for additive in additives:
            db_additive = await Additive.objects.get_or_none(name=additive)

            if not db_additive:
                raise Exception(f"Invalid additive: {additive}")

            price += db_additive.dict()["price"]

        return price
