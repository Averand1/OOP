from item import Item

class Phone(Item):
    all = []
    def __init__(self, name: str  , price:float, quantity=0, broken_phones=0): 
        #Call to super function to have access to all attributes / method
        super().__init__(
            name, price, quantity
        )
        # run validations to receieved arguments

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero"
        
        # Assign to self object

        self.broken_phones = broken_phones
        
        # Actions to execute
        Phone.all.append(self)
