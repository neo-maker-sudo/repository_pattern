from django.db import models
from product_business.domain import model as domain_model


class Product(models.Model):
    name = models.CharField(max_length=32, null=False)
    price = models.IntegerField()
    total = models.IntegerField()

    @staticmethod
    def add_from_domain(product: domain_model.Product):
        product = Product.objects.create(
            name=product.name, price=product.price, total=product.total
        )

    def to_domain(self):
        return domain_model.Product(name=self.name, price=self.price, total=self.total)
