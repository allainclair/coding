from pytest import fixture
from app.schemas import Summary


@fixture
def summary() -> Summary:
    return Summary(summary="Any summary")
