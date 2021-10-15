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
    
    def apply_discount(self):
        self.price = self.price + Item.pay_rate


    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item(1, 12, 5) 
item2 = Item("Laptop", 1000, 3)

print(Item.__dict__) #Gives all the attributes for Class level
print(item1.__dict__) #Gives all the attributes for instance level




#init (constructor) __init__
item1 = Item("Phone" , 4, 12) 
item1.apply_discount()
# print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 #Pay rate is now 30%
item2.apply_discount()
print(item2.price)





