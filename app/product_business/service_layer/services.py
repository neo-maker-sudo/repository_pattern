from app.product_business.domain import model as domain_model
from app.product_business.adapters.repository import AbstractRepository


def create_product(
    name: str, price: int, total: int, repo: AbstractRepository
) -> domain_model.Product:
    product = domain_model.Product(name=name, price=price, total=total)
    repo.session.commit()

    return product


def retrieve_product(product_id: int, repo: AbstractRepository) -> domain_model.Product:
    product = repo.get(product_id)

    if product is None:
        raise domain_model.ProductNotExist

    return product
