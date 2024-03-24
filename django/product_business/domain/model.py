
# 業務邏輯層的領域模型
class Product:
    def __init__(self, name: str, price: int, total: int):
        self.name = name
        self.price = price
        self.total = total

    def __repr__(self):
        return f"<Product {self.name}>"
