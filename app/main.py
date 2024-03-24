from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

from app.product_business import service_layer as services
from app.product_business.domain import model as domain_model
from app.product_business.adapters.repository import ProductRepository
from app.sql import start_mapper, get_db


app = FastAPI()
start_mapper()


class ProductSchemaIn(BaseModel):
    name: str
    price: int
    total: int


@app.get("/products/{product_id}")
def retrieve_product_view(product_id: int, session=Depends(get_db)):
    try:
        product = services.retrieve_product(
            product_id, ProductRepository(session=session)
        )

    except domain_model.ProductNotExist:
        raise HTTPException(
            detail="Product not Exist", status_code=status.HTTP_404_NOT_FOUND
        )

    return product


@app.post("/products")
def create_product_view(schema: ProductSchemaIn, session=Depends(get_db)):

    product = services.create_product(
        name=schema.name,
        price=schema.price,
        total=schema.total,
        repo=ProductRepository(session=session),
    )

    return {
        "name": product.name,
        "price": product.price,
        "total": product.total,
    }
