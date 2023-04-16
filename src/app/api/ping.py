from beartype import beartype
from fastapi import APIRouter
from pydantic import BaseModel
from semver.version import Version

from app import __version__
from app.config import ENVIRONMENT, Environment

router = APIRouter()


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
