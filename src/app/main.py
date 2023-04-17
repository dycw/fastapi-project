from logging import getLogger

from beartype import beartype
from fastapi import FastAPI

from app.api import home, ping, summaries
from app.db import init_db
from app.db_sqla.engines import ENGINE
from app.db_sqla.schemas.all import create_tables

_logger = getLogger("uvicorn")


@beartype
def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(home.router)
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    _logger.info("Starting up...")
    init_db(app)
    create_tables(ENGINE)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    _logger.info("Shutting down...")
