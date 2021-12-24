

class CheckOut:
    def __init__(self) -> None:
        self.total = 0
        self.itemsInCart = {}
        
    def addItemPrice(self, item, price):
        self.itemsInCart[item]=price

    
    def addItem(self, item):
        self.total += self.itemsInCart[item]
    
    def getTotal(self):
        return self.total