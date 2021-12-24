import pytest
from app import CheckOut


@pytest.fixture()
def checkoutInstance():
    co = CheckOut()
    co.addItemPrice("a",1)
    co.addItemPrice("b",2)
    return co
    
def test_AddItem(checkoutInstance):
    checkoutInstance.addItem("a")
    checkoutInstance.addItem("b")

def testException(checkoutInstance):
    with pytest.raises(Exception):
        checkoutInstance.addItem("unknown")
    

def test_calculateTotal(checkoutInstance):
    checkoutInstance.addItem("a")
    checkoutInstance.addItem("a")
    checkoutInstance.addItem("b")
    assert checkoutInstance.getTotal() == 4
