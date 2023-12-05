from psycopg import AsyncConnection
from uuid import uuid4, UUID
from app.schemas import RequestProduct, DBProduct, ProductModel, Category, DBCategory
from logging import getLogger

logger = getLogger(__name__)


# Add .env
DB_NAME = "mydb"
DB_USER = "postgres"
DB_USER_PASSWORD = "postgres"
HOST = "localhost"

db_connection: AsyncConnection | None = None


async def get_db_connection() -> AsyncConnection:
    global db_connection
    if db_connection is None:
        db_connection = await _create_connection()
        logger.info("DB connection created")
        return db_connection
    else:
        return db_connection


async def close_db_connection() -> None:
    global db_connection
    if db_connection is not None:
        await db_connection.close()
        logger.info("DB connection closed")
        db_connection = None


async def add_category(category: Category) -> DBCategory:
    db_category = DBCategory(id=uuid4(), **category.dict())
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute(
            "INSERT INTO category (id, name, description) VALUES (%s, %s, %s)",
            (db_category.id, db_category.name, db_category.description),
        )
    await async_conn.commit()
    return db_category


async def add_product(request_product: RequestProduct) -> DBProduct:
    db_product = DBProduct(id=uuid4(), **request_product.dict())
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute(
            "INSERT INTO product (id, category_id, name, price, description) VALUES (%s, %s, %s, %s, %s)",
            (db_product.id, db_product.category_id, db_product.name, db_product.price, db_product.description),
        )
    await async_conn.commit()
    return db_product


async def get_category_by_id(category_id: UUID) -> DBCategory:
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute("SELECT * FROM category WHERE id = %s", (category_id,))
        row = await async_cursor.fetchone()
        return DBCategory(id=row[0], name=row[1], description=row[2])


async def get_product_and_its_category_by_id(product_id: UUID) -> tuple[DBProduct, DBCategory]:
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute("SELECT * FROM product p JOIN category c ON p.category_id = c.id WHERE p.id = %s", (product_id,))
        row = await async_cursor.fetchone()
        db_product = DBProduct(id=row[0], name=row[1], price=row[2], description=row[3], category_id=row[4])
        db_category = DBCategory(id=row[5], name=row[6], description=row[7])
        return db_product, db_category


async def get_all_categories() -> list[DBCategory]:
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute("SELECT * FROM category")
        rows = await async_cursor.fetchall()
        db_categories = []
        for row in rows:
            db_categories.append(DBCategory(id=row[0], name=row[1], description=row[2]))
        return db_categories


async def get_all_products_and_its_categories() -> list[tuple[DBProduct, DBCategory]]:
    async_conn = await get_db_connection()
    async with async_conn.cursor() as async_cursor:
        await async_cursor.execute("SELECT * FROM product p JOIN category c ON p.category_id = c.id")
        rows = await async_cursor.fetchall()
        tuples = []
        for row in rows:
            db_product = DBProduct(id=row[0], name=row[1], price=row[2], description=row[3], category_id=row[4])
            db_category = DBCategory(id=row[5], name=row[6], description=row[7])
            tuples.append((db_product, db_category))
        return tuples


async def _create_connection() -> AsyncConnection:
    return await AsyncConnection.connect(
        f"dbname={DB_NAME} host={HOST} user={DB_USER} password={DB_USER_PASSWORD}")