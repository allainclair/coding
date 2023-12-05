from fastapi import status
from httpx import AsyncClient
import json
from urllib.parse import urljoin
from uuid import uuid4
from decimal import Decimal
from pytest import fixture
from app.schemas import RequestProduct, Category, DBCategory, DBProduct, CartRequest, CartProductRequest
from pytest import mark

HOST = "http://127.0.0.1:8000"


@mark.usefixtures("manage_db")
async def test_create_category_ok(category_1: Category,) -> None:
    url = urljoin(HOST, "categories")
    async with AsyncClient() as client:
        response = await client.post(url, json=category_1.dict())
    assert response.status_code == status.HTTP_200_OK


@mark.usefixtures("manage_db")
async def test_create_product_ok(request_product_1: RequestProduct) -> None:
    url = urljoin(HOST, "products")
    async with AsyncClient() as client:
        response = await client.post(url, json=json.loads(request_product_1.json()))
    assert response.status_code == status.HTTP_200_OK


@mark.usefixtures("manage_db")
async def test_get_all_categories_ok(db_categories: list[DBCategory]) -> None:
    url = urljoin(HOST, "categories")
    async with AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


@mark.usefixtures("manage_db")
async def test_get_product_by_id_ok(db_product_1: DBProduct) -> None:
    url = urljoin(HOST, f"products/{db_product_1.id}")
    async with AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@mark.usefixtures("manage_db")
async def test_get_all_products_ok(db_products: list[DBProduct]) -> None:
    url = urljoin(HOST, "products")
    async with AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


@mark.usefixtures("manage_db")
async def test_manage_cart(db_products: list[DBProduct]) -> None:
    id_ = str(uuid4())
    url = urljoin(HOST, f"cart/{id_}")
    async with AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    print(response.json())

    cart_request = CartRequest(
        id=id_,
        products=[CartProductRequest(product_id=product.id, quantity=1) for product in db_products]
    )
    cart_request_dict = json.loads(cart_request.json())
    url = urljoin(HOST, f"cart")
    async with AsyncClient() as client:
        response = await client.put(url, json=cart_request_dict)
    assert response.status_code == status.HTTP_200_OK
    print(response.json())

    url = urljoin(HOST, f"cart/{id_}")
    async with AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    print(response.json())
