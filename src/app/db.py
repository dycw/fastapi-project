from logging import getLogger

from beartype import beartype
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from app.config import SETTINGS

_logger = getLogger("uvicorn")


TORTOISE_ORM = {
    "connections": {"default": SETTINGS.database_url},
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        }
    },
}


@beartype
def init_db(app: FastAPI, /) -> None:
    register_tortoise(
        app,
        db_url=SETTINGS.database_url,
        modules={"models": ["app.models.tortoise"]},
        add_exception_handlers=True,
    )


@beartype
async def generate_schema() -> None:
    _logger.info("Initializing Tortoise...")
    await Tortoise.init(
        db_url=SETTINGS.database_url, modules={"models": ["models.tortoise"]}
    )
    _logger.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
