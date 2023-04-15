from enum import StrEnum, auto
from functools import lru_cache
from logging import getLogger
from typing import cast

from beartype import beartype
from pydantic import AnyUrl, BaseSettings
from typed_settings import find, settings
from utilities.typed_settings import load_settings

_LOGGER = getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = cast(bool, 0)
    database_url: AnyUrl = cast(AnyUrl, None)


@lru_cache
@beartype
def get_settings() -> Settings:
    _LOGGER.info("Loading config settings from the environment...")
    return Settings()


class Environment(StrEnum):
    development = auto()
    staging = auto()
    production = auto()


@settings
class EnvironmentSettings:
    environment: Environment = Environment.development


ENVIRONMENT = load_settings(
    EnvironmentSettings, appname="app", config_files=[find("pyproject.toml")]
).environment
