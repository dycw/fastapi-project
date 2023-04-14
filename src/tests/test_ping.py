from re import search

from beartype import beartype
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


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
