import os

import strawberry
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from additive.api import AdditiveQuery, additive_router
from cart.api import CartMutation, CartQuery
from db import database, engine, media_dir, metadata, static_dir
from pizza.api import PizzaQuery, pizza_router
from ticket.api import TicketMutation, TicketQuery
from user.api import UserMutation, UserQuery

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@strawberry.type
class Query(PizzaQuery, CartQuery, AdditiveQuery, UserQuery, TicketQuery):
    pass


@strawberry.type
class Mutation(UserMutation, CartMutation, TicketMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
app.include_router(pizza_router)
app.include_router(additive_router)


@app.get("/media/{name}", response_class=FileResponse)
async def get_media(name: str):
    return os.path.join(media_dir, name)


@app.get("/static/{name}", response_class=FileResponse)
async def get_static_media(name: str):
    return os.path.join(static_dir, name)


if __name__ == "__main__":
    uvicorn.run(app, debug=True, use_colors=True)
