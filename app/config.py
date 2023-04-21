from typing import Any, cast

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")


SETTINGS: Settings = cast(Any, Settings)()
