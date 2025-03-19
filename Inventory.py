from itertools import product


class Product:
    name:str
    price: float

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Inventory:
    products = []

    def __init__(self):
        self.products = []

    def add_product(self,product: Product):
        pass

    def remove_product(self,product_name: str):
        pass

    def get_product(self,product_name: str)-> Product :
        pass

    def total_inventory_value(self) -> float:
        pass








