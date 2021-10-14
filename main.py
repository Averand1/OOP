#Creation of class

class Item:
    pay_rate = 0.8  #The pay after 20% discount
    def __init__(self, name: str, price: float, quantity=0): 
        # run validations to receieved arguments
        assert price >=0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        return self.price * self.quantity

#init (constructor) __init__
item1 = Item("Phone" , 4, 12) 
item2 = Item("Laptop", 1000, 3)

print()





