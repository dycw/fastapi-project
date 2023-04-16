from collections.abc import Iterator

from app.config import SETTINGS
from app.main import create_application
from fastapi.testclient import TestClient
from pytest import fixture
from tortoise.contrib.fastapi import register_tortoise


@fixture(scope="module")
def test_app() -> Iterator[TestClient]:
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client


@fixture(scope="module")
def test_app_with_db() -> Iterator[TestClient]:
    app = create_application()
    register_tortoise(
        app,
        db_url=SETTINGS.database_test_url,
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:
        yield test_client
