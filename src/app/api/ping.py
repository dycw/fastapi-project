from beartype import beartype
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from semver.version import Version

from app import __version__
from app.config import ENVIRONMENT, Environment, Settings, get_settings

router = APIRouter()


@router.get("/ping")
@beartype
async def pong(*, settings: Settings = Depends(get_settings)) -> dict[str, str | bool]:
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }


class _DebugModel(BaseModel):
    environment: Environment
    version: tuple[int, int, int]


@router.get("/debug")
@beartype
async def debug() -> _DebugModel:
    version = Version.parse(__version__)
    return _DebugModel(
        environment=ENVIRONMENT, version=(version.major, version.minor, version.patch)
    )
