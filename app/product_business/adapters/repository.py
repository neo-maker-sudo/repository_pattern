from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Session
from app.product_business.domain import model as domain_model


class AbstractRepository(object, metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError


class ProductRepository(AbstractRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, product: domain_model.Product) -> None:
        self.session.add(product)

    def get(self, product_id: int) -> domain_model.Product:
        return self.session.get(domain_model.Product, product_id)
