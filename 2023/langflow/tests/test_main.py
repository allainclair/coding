from fastapi import status
from httpx import AsyncClient
from pytest import fixture, mark
from urllib.parse import urljoin
from tests.constants import HOST
from unittest.mock import Mock, AsyncMock
from app.schemas import Summary, Query
from app.services import SummaryService
from collections.abc import AsyncIterator
from app.main import app


@fixture
async def client_overrides_summary_service(summary: Summary) -> AsyncIterator[AsyncClient]:
    def _summary_service_instance(query: Query) -> Mock:
        """Override the SummaryService, we can think this like the __init__."""
        instance = AsyncMock()
        instance.get_summary.return_value = summary
        return instance

    app.dependency_overrides[SummaryService] = _summary_service_instance
    async with AsyncClient(app=app) as client:
        yield client
    app.dependency_overrides = {}


async def test_query_ok(
    client_overrides_summary_service: AsyncClient,
    summary: Summary,
) -> None:
    url = urljoin(HOST, "search")
    response = await client_overrides_summary_service.post(url, json={"query": "query!"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == summary.dict()


async def test_query_not_a_query(client_overrides_summary_service: AsyncClient) -> None:
    url = urljoin(HOST, "search")
    response = await client_overrides_summary_service.post(url, json={"not_a_query": "not_a_query!"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
