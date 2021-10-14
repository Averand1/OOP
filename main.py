#Creation of class

class Item:
    def __init__(self, name:str, price:float, quantity=0): ##can set args=0 if YDk what to pass
        #print(f"I am created: {name}") #f lets us use string literal
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

#python takes the object itself (item1) and send it as an argument to the method

#init (constructor) __init__
item1 = Item(1, 12, 5) 
item2 = Item("Laptop", 1000, 3)






