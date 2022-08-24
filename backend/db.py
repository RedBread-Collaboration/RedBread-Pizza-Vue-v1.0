import os
from uuid import uuid4

import databases
import ormar
import sqlalchemy
from pydantic import BaseModel

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")

media_dir = os.path.join(os.getcwd(), "media/media")
print(media_dir)
static_dir = os.path.join(os.getcwd(), "media/static")
valid_file_types = ["image/png", "image/jpeg", "image/bmp", "image/svg+xml"]


def get_uuid():
    return str(uuid4())


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Message(BaseModel):
    message: str
