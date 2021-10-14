#Creation of class

class Item:
    def __init__(self, name:str, price:float, quantity=0): ##can set args=0 if YDk what to pass
        #print(f"I am created: {name}") #f lets us use string literal
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price + Item.pay_rate


    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone", 12, 5) 
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





