import pytest

from Inventory import Inventory

@pytest.fixture()
def inventory():
    return Inventory()

