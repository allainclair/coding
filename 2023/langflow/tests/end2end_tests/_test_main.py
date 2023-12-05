from httpx import AsyncClient
from fastapi import status
from tests.constants import HOST
from icecream import ic


async def test_query() -> None:
    async with AsyncClient(base_url=HOST) as client:
        response = await client.post(
            "/search",
            json={"query": "what happened to SVB? Make a big text"},
            timeout=25,
        )
        assert response.status_code == status.HTTP_200_OK
        ic(response.json())
