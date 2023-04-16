from collections.abc import Iterator
from typing import Any

from beartype import beartype
from sqlalchemy import Engine
from utilities.modules import yield_module_subclasses

from app.db_sqla import schemas
from app.db_sqla.schemas.base import Base


@beartype
def yield_models() -> Iterator[type[Any]]:
    return yield_module_subclasses(schemas, Base, recursive=True)


@beartype
def create_tables(engine: Engine, /) -> None:
    _ = list(yield_models())
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)
