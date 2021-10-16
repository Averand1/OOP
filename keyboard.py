from item import Item

class Keyboard(Item):
    all = []
    def __init__(self, name: str  , price:float, quantity=0,): 
        #Call to super function to have access to all attributes / method
        super().__init__(
            name, price, quantity
        )
