from abc import ABCMeta, abstractmethod
from products import models as django_models
from product_business.domain import model as domain_model


class AbstractRepository(object, metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError


class ProductRepository(AbstractRepository):

    def add(self, product: domain_model.Product) -> None:
        # 從領域模型新增 product
        django_models.Product.add_from_domain(product=product)

    def get(self, product_id: int) -> domain_model.Product:
        # 從 django ORM 資料庫模型取得資料庫實例再手動轉為領域模型
        return django_models.Product.objects.get(pk=product_id).to_domain()
