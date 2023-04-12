from beartype import beartype
from fastapi import FastAPI
import app.routes.front.home


@beartype
def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(app.routes.front.home.router)
    return application
