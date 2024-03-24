from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.orm import registry
from app.product_business.domain import model as domain_model


mapper_registry = registry()

products = Table(
    "products",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(64), unique=True, nullable=False),
    Column("price", Integer),
    Column("total", Integer),
)


def start_mapper():
    mapper_registry.map_imperatively(domain_model.Product, products)
