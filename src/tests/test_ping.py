from re import search

from app.config import Environment
from beartype import beartype
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


@beartype
def test_env(*, test_app: TestClient) -> None:
    response = test_app.get("/environment")
    assert response.status_code == HTTP_200_OK
    assert set(json := response.json()) == {"environment"}
    environment = Environment[json["environment"]]
    assert environment in Environment


@beartype
def test_ping(*, test_app: TestClient) -> None:
    response = test_app.get("/ping")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": "True"}


@beartype
def test_version(*, test_app: TestClient) -> None:
    response = test_app.get("/version")
    assert response.status_code == HTTP_200_OK
    assert set(json := response.json()) == {"version"}
    version = json["version"]
    assert search(r"^(\d+)\.(\d+)\.(\d+)$", version)
