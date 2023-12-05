from app.schemas import ProductModel, RequestProduct, CartRequest, CartResponse, CartProductResponse
from uuid import UUID
from app.db import add_product, get_category_by_id, get_product_and_its_category_by_id, get_all_products_and_its_categories
from redis.asyncio import Redis
import json
redis = Redis(host='localhost', port=6379, db=0)


async def create_product_service(new_product: RequestProduct) -> ProductModel:
    db_product = await add_product(new_product)
    db_category = await get_category_by_id(db_product.category_id)
    return ProductModel(**db_product.dict(), category=db_category)


async def get_product_by_id(product_id: UUID) -> ProductModel:
    db_product, db_category = await get_product_and_its_category_by_id(product_id)
    return ProductModel(**db_product.dict(), category=db_category)


async def get_all_products() -> list[ProductModel]:
    all_products = []
    db_products_and_categories = await get_all_products_and_its_categories()
    for prod, category in db_products_and_categories:
        all_products.append(ProductModel(**prod.dict(), category=category))
    return all_products


async def update_cart_service(cart_request: CartRequest) -> CartResponse:
    redis_products = []
    cart_products = []
    for product in cart_request.products:
        product_model = await get_product_by_id(product.product_id)
        cart_product = CartProductResponse(**product_model.dict(), quantity=product.quantity)
        cart_products.append(cart_product)
        redis_products.append(json.loads(cart_product.json()))
    await redis.set(str(cart_request.id), json.dumps(redis_products))
    return CartResponse(id=cart_request.id, products=cart_products)


async def get_cart_service(cart_id: UUID) -> None | CartResponse:
    redis_products = await redis.get(str(cart_id))
    if redis_products is None:
        return CartResponse(id=cart_id, products=[])
    else:
        return CartResponse(id=cart_id, products=[CartProductResponse(**p) for p in json.loads(redis_products)])

    # products = []
    # for product_id in cart_request.products:
    #     product_model = await get_product_by_id(product_id)
    #     products.append(json.loads(product_model.json()))
    # await redis.set(str(cart_request.id), json.dumps(products))
