from pydantic import BaseModel, Field
from uuid import UUID


class Category(BaseModel):
    name: str
    description: str | None = None


class DBCategory(Category):
    id: UUID


class BaseProduct(BaseModel):
    name: str
    price: float
    description: str | None = None


class RequestProduct(BaseProduct):
    category_id: UUID


class DBProduct(RequestProduct):
    id: UUID


class ProductModel(BaseProduct):
    id: UUID
    category: DBCategory


class CartProductRequest(BaseModel):
    product_id: UUID
    quantity: int = Field(..., gt=0)


class CartProductResponse(ProductModel):
    quantity: int = Field(..., gt=0)


class CartRequest(BaseModel):
    id: UUID  # It can be a UserID for example. Because we can have only one cart for a user.
    products: list[CartProductRequest]


class CartResponse(BaseModel):
    id: UUID  # It can be a UserID for example. Because we can have only one cart for a user.
    products: list[CartProductResponse]
