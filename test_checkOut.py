import pytest
from app import CheckOut


@pytest.fixture()
def checkoutInstance():
    co = CheckOut()
    return co


def test_check_addItemPrice(checkoutInstance):
    checkoutInstance.addItemPrice("a",1)

def test_AddItem(checkoutInstance):
    checkoutInstance.addItem("a")
