from app.db_sqla.schemas.all import yield_models
from beartype import beartype


class TestYieldModels:
    @beartype
    def test_count(self) -> None:
        assert len(list(yield_models())) == 1
