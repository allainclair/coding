from fastapi import FastAPI, Depends
from typing import Annotated
from app.schemas import DBCategory, ProductModel, CartResponse
from app.service import create_product_service, get_product_by_id, get_all_products, update_cart_service, get_cart_service
from app.db import get_all_categories, add_category


app = FastAPI()


@app.post("/categories")
async def create_category(db_category: Annotated[DBCategory, Depends(add_category)]) -> DBCategory:
    return db_category


@app.post("/products")
async def create_product(product: Annotated[ProductModel, Depends(create_product_service)]) -> ProductModel:
    return product


@app.get("/categories")
async def get_categories(db_categories: Annotated[list[DBCategory], Depends(get_all_categories)]) -> list[DBCategory]:
    return db_categories


@app.get("/products/{product_id}")
async def get_product(product_model: Annotated[ProductModel, Depends(get_product_by_id)]) -> ProductModel:
    return product_model


@app.get("/products")
async def get_products(db_products: Annotated[list[ProductModel], Depends(get_all_products)]) -> list[ProductModel]:
    return db_products


@app.get("/cart/{cart_id}")
async def get_cart(cart: Annotated[CartResponse, Depends(get_cart_service)]) -> CartResponse:
    return cart


@app.put("/cart")
async def update_cart(cart: Annotated[CartResponse, Depends(update_cart_service)]) -> CartResponse:
    return cart