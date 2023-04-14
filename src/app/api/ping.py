from beartype import beartype
from fastapi import APIRouter, Depends

from app import __version__
from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
@beartype
async def pong(*, settings: Settings = Depends(get_settings)) -> dict[str, str | bool]:
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@router.get("/version")
@beartype
async def version() -> dict[str, str]:
    return {"version": __version__}
