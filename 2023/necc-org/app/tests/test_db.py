from app.db import add_product, add_category, get_all_categories, get_db_connection, get_product_and_its_category_by_id
from app.schemas import RequestProduct, DBProduct, DBCategory, Category
from pytest import fixture, mark


@fixture
async def manage_db() -> None:
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute("DELETE FROM product")
        await async_cursor.execute("DELETE FROM category")
    await async_conn.commit()



@fixture
def category_1() -> Category:
    return Category(name="Category 1", description="Category 1 description")


@fixture
def category_2() -> Category:
    return Category(name="Category 2", description="Category 2 description")


@fixture
async def db_category_1(category_1: Category) -> DBCategory:
    db_category = await add_category(category_1)
    assert Category(**db_category.dict()) == category_1
    return db_category


@fixture
async def db_category_2(category_2: Category) -> DBCategory:
    db_category = await add_category(category_2)
    assert Category(**db_category.dict()) == category_2
    return db_category


@fixture
def db_categories(db_category_1: DBCategory, db_category_2: DBCategory) -> list[DBCategory]:
    return [db_category_1, db_category_2]


@fixture
def request_product_1(db_category_1: DBCategory) -> RequestProduct:
    return RequestProduct(name="Product 1", price=10., description="Product 1 description", category_id=db_category_1.id)


@fixture
def request_product_2(db_category_2: DBCategory) -> RequestProduct:
    return RequestProduct(name="Product 2", price=20., description="Product 2 description", category_id=db_category_2.id)


@fixture
def request_product_3(db_category_2: DBCategory) -> RequestProduct:
    return RequestProduct(name="Product 3", price=30., description="Product 3 description", category_id=db_category_2.id)


@fixture
async def db_product_1(request_product_1: RequestProduct) -> DBProduct:
    db_product = await add_product(request_product_1)
    assert RequestProduct(**db_product.dict()) == request_product_1
    return db_product


@fixture
async def db_product_2(request_product_2: RequestProduct) -> DBProduct:
    db_product = await add_product(request_product_2)
    assert RequestProduct(**db_product.dict()) == request_product_2
    return db_product


@fixture
async def db_product_3(request_product_3: RequestProduct) -> DBProduct:
    db_product = await add_product(request_product_3)
    assert RequestProduct(**db_product.dict()) == request_product_3
    return db_product


@fixture
def db_products(db_product_1: DBProduct, db_product_2: DBProduct, db_product_3: DBProduct) -> list[DBProduct]:
    return [db_product_1, db_product_2, db_product_3]


@mark.usefixtures("manage_db")
async def test_add_and_get_categories_and_products(db_categories: list[DBCategory], db_products: list[DBProduct]) -> None:
    # assert await get_all_categories() == db_categories
    # assert await get_all_products() == db_products
    first_db_product = db_products[0]
    db_product, db_category = await get_product_and_its_category_by_id(first_db_product.id)
    assert (db_product, db_category) == (first_db_product, db_categories[0])


@mark.usefixtures("manage_db")
def test_clean() -> None:
    pass
