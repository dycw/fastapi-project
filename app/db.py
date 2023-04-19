from typing import cast

from databases import Database
from ormar import Boolean, Integer, Model, ModelMeta, String
from sqlalchemy import MetaData, create_engine

from app.config import SETTINGS

database = Database(SETTINGS.db_url)
metadata = MetaData()


class BaseMeta(ModelMeta):
    database = database
    metadata = metadata


class User(Model):
    class Meta(BaseMeta):  # type: ignore[]
        tablename = "users"

    id = cast(int, Integer(primary_key=True))  # noqa: A003
    email = cast(str, String(max_length=128, unique=True, nullable=False))
    active = Boolean(default=True, nullable=False)


engine = create_engine(SETTINGS.db_url)
metadata.create_all(engine)
