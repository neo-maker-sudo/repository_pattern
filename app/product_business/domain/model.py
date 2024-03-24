class Product:
    def __init__(self, name: str, price: int, total: int):
        self.name = name
        self.price = price
        self.total = total


class ProductNotExist(Exception):
    pass
