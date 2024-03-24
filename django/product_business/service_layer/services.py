from product_business.adapters.repository import AbstractRepository
from product_business.domain import model as domain_model


def create_product(
    product_name: str, price: int, total: int, repo: AbstractRepository
) -> None:
    # 建立 Product 領域模型
    product = domain_model.Product(name=product_name, price=price, total=total)

    repo.add(product)


def retrieve_product(product_id: int, repo: AbstractRepository) -> domain_model.Product:
    return repo.get(product_id)
