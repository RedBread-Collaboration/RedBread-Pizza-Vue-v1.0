import os
import sqlite3
from typing import List

import aiofiles
import strawberry
from db import Message, get_uuid, media_dir, valid_file_types
from fastapi import APIRouter, File, UploadFile
from fastapi import status as status_code
from fastapi.responses import JSONResponse

from .models import Additive, GraphQLAdditive
from .schemas import CreateAdditive, GetAdditive

additive_router = APIRouter(prefix='/additive', tags=["additive"])


@strawberry.type
class AdditiveQuery:

    @strawberry.field
    async def additive(self) -> List[GraphQLAdditive]:
        return await Additive.objects.all()


@additive_router.post("/", response_model=GetAdditive, responses={409: {"model": Message}, 403: {"model": Message}})
async def create_pizza(name: str, price: int, photo: UploadFile = File(...)):
    try:
        file_name = f"ADDITIVE_{get_uuid()}_{photo.filename}"
        file_path = os.path.join(media_dir, file_name)

        if photo.content_type in valid_file_types:
            additive = CreateAdditive(name=name, photo=file_name, price=price)

            async with aiofiles.open(file_path, "wb") as buffer:
                data = await photo.read()
                await buffer.write(data)

            return await Additive.objects.create(id_=get_uuid(), **additive.dict())

        return JSONResponse(status_code=status_code.HTTP_403_FORBIDDEN,
                            content={"message": f"Wrong file type. Valid types: {valid_file_types}"})

    except sqlite3.IntegrityError:
        return JSONResponse(status_code=status_code.HTTP_409_CONFLICT,
                            content={"message": "Pizza with that name already exists"})

    except Exception as err:
        return JSONResponse(status_code=status_code.HTTP_403_FORBIDDEN, content={"message": f"Unknown error: {err}"})
