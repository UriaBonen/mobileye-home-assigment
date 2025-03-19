import random
from idlelib.util import py_extensions
from itertools import product

import pytest

from Inventory import Product
from conftest import inventory
from data import products


@pytest.mark.parametrize("product", products)
def test_add_item(inventory, product):
    inventory.add_product(product=product)
    assert len(inventory.products) == 1
    assert inventory.is_product_exist(product=product) == True


@pytest.mark.parametrize("product", products)
def test_get_item(inventory, product):
    inventory.add_product(product=product)
    product_ = inventory.get_product(product_name=product.name)
    assert inventory.is_product_exist(product=product_) == True
    assert product_.price == product.price


@pytest.mark.parametrize("product", products)
def test_remove_item(inventory, product):
    inventory.add_product(product=product)
    assert len(inventory.products) == 1
    assert inventory.is_product_exist(product=product) == True
    inventory.remove_product(product_name=product.name)
    assert inventory.is_product_exist(product=product) == False


def test_calculate_total_prices(inventory):
    total_price = 0
    for product in products:
        inventory.add_product(product)
        total_price += product.price
    assert total_price == inventory.total_inventory_value()

def test_negative_product_price(inventory):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("Invalid Product", -10)

def test_get_non_existing_product(inventory):
    product = random.choice(products)
    assert inventory.get_product(product) is None



