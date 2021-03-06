#Creation of class
import csv

class Item:
    pay_rate = 0.8  #The pay after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): 
        # run validations to receieved arguments
        assert price >=0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price + Item.pay_rate

    @classmethod
    def instantiate_self_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #list of dictionaries
            items = list(reader) #converts to list
        
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        #We will count out decimal ending with point 0
        #For i.e: 5.0, 12.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

#Inheritance
class Phone(Item):
    all = []
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0): 
        #Call to super function to have access to all attributes / method
        super().__init__(
            name, price, quantity
        )
        # run validations to receieved arguments
        assert price >=0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
        
        # Actions to execute
        Phone.all.append(self)

phone1 = Phone("JSPhone1", 500, 5, 1)

print(Item.all)
print(Phone.all)
