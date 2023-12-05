from pytest import fixture
from app.schemas import Cart, Product
from decimal import Decimal


@fixture
def product_1() -> Product:
    return Product(id="1", name="Product 1", price=Decimal("10"))


@fixture
def product_2() -> Product:
    return Product(id="2", name="Product 2", price=Decimal("20"), description="Product 2 description")


@fixture
def cart(product_1: Product, product_2: Product) -> Cart:
    return Cart(products=[product_1, product_2])


def test_cart_price(cart: Cart) -> None:
    assert cart.price == Decimal("30")
