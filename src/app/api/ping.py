from beartype import beartype
from fastapi import APIRouter
from pydantic import BaseModel

from app import VERSION
from app.config import ENVIRONMENT, Environment

router = APIRouter()


class _DebugModel(BaseModel):
    environment: Environment
    version: tuple[int, int, int]


@router.get("/debug")
@beartype
async def debug() -> _DebugModel:
    return _DebugModel(
        environment=ENVIRONMENT, version=(VERSION.major, VERSION.minor, VERSION.patch)
    )
