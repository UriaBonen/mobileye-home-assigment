from itertools import product
from os import name


class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self.price = price
        else:
            raise ValueError("Price cannot be negative")


    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Product(name='{self.name}', price={self.price})"


class Inventory:
    products = []

    def __init__(self):
        self.products = []

    def _is_empty_list(self) -> bool:
        if len(self.products) == 0:
            print("The inventory list is empty")
            return True
        else:
            return False

    def is_product_exist(self, product: Product) -> bool:
        if not self._is_empty_list():
            for product_ in self.products:
                if product.name == product_.name:
                    print(f"{product.name} is already exist")
                    return True
            return False
        else:
            return False

    @classmethod
    def clear_products(cls):
        cls.products.clear()

    def add_product(self, product: Product):
        if not self.is_product_exist(product=product):
            self.products.append(product)

    def remove_product(self, product_name: str):
        if not self._is_empty_list():
            for product in self.products:
                if product.name == product_name:
                    self.products.remove(product)
                    print(f"Product '{name}' removed.")
            print(f"Product with name '{name}' not found.")

    def get_product(self, product_name: str) -> Product:
        if not self._is_empty_list():
            for product in self.products:
                if product_name == product.name:
                    return product
            print(f"{product_name} product is not exist")
            return None

    def total_inventory_value(self) -> float:
        if not self._is_empty_list():
            total_inventory_value = 0
            for product in self.products:
                total_inventory_value += product.price
            print(f"The total inventories is: {total_inventory_value} ")
            return total_inventory_value

    def __str__(self):
        return '\n'.join(str(product) for product in self.products)
