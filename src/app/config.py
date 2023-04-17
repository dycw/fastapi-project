from enum import StrEnum, auto

from typed_settings import find, settings
from utilities.typed_settings import load_settings


class Environment(StrEnum):
    """An enumeration of the environments."""

    development = auto()
    staging = auto()
    production = auto()


@settings
class EnvironmentChoiceSettings:
    """Settings dictating the choice of an environment."""

    environment: Environment = Environment.development


ENVIRONMENT = load_settings(
    EnvironmentChoiceSettings,
    appname="app",
    config_files=[find("pyproject.toml")],
    config_file_section="environment",
).environment


@settings
class EnvironmentSettings:
    """Settings for a given environment."""

    database_url: str
    database_test_url: str
    database_url_sqla: str
    database_test_url_sqla: str


SETTINGS = load_settings(
    EnvironmentSettings,
    appname="app",
    config_files=[find("pyproject.toml")],
    config_file_section=f"app.{ENVIRONMENT.name}",
)
