from app.config import Environment
from beartype import beartype
from fastapi.testclient import TestClient
from semver.version import Version
from starlette.status import HTTP_200_OK


@beartype
def test_debug(*, test_app: TestClient) -> None:
    response = test_app.get("/debug")
    assert response.status_code == HTTP_200_OK
    assert set(json := response.json()) == {"environment", "version"}
    assert isinstance(Environment[json["environment"]], Environment)
    assert isinstance(Version(*json["version"]), Version)
