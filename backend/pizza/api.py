import os
import sqlite3
from typing import List

import aiofiles
import strawberry
from db import Message, get_uuid, media_dir, valid_file_types
from fastapi import APIRouter, File, UploadFile
from fastapi import status as status_code
from fastapi.responses import JSONResponse

from .models import GraphQLPizza, PizzaTemplate
from .schemas import CreatePizza, GetPizza

pizza_router = APIRouter(prefix='/pizza', tags=["pizza"])


@strawberry.type
class PizzaQuery:

    @strawberry.field
    async def pizza(self) -> List[GraphQLPizza]:
        return await PizzaTemplate.objects.all()


@pizza_router.post("/", response_model=GetPizza, responses={409: {"model": Message}, 403: {"model": Message}})
async def create_pizza_item(name: str,
                            ingredients: str,
                            price_small: int,
                            price_medium: int,
                            price_large: int,
                            photo: UploadFile = File(...)):
    try:
        file_name = f"PIZZA_{get_uuid()}_{photo.filename}"
        file_path = os.path.join(media_dir, file_name)
        print(file_name)

        if photo.content_type in valid_file_types:

            pizza = CreatePizza(name=name,
                                ingredients=ingredients,
                                photo=file_name,
                                price_small=price_small,
                                price_medium=price_medium,
                                price_large=price_large)

            async with aiofiles.open(file_path, "wb") as buffer:
                data = await photo.read()
                await buffer.write(data)

            return await PizzaTemplate.objects.create(id_=get_uuid(), **pizza.dict())

        return JSONResponse(status_code=status_code.HTTP_403_FORBIDDEN,
                            content={"message": f"Wrong file type. Valid types: {valid_file_types}"})

    except sqlite3.IntegrityError:
        return JSONResponse(status_code=status_code.HTTP_409_CONFLICT,
                            content={"message": "Pizza with that name already exists"})

    except Exception as err:
        return JSONResponse(status_code=status_code.HTTP_403_FORBIDDEN, content={"message": f"Unknown error: {err}"})
