import csv


class Item:
    pay_rate = 0.8 #The pay after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): 
        # run validations to receieved arguments
        assert price >=0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Assign to self object
        self.__name = name  #can't set value when Read Only attribute is made that's why we use _name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    #Property decorator: Read-Only attributes
    def name(self):
        print("You are trying to get name")
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price + Item.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
 
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @property ##Changes things to read only attribute, use @name.setter to set value
    def read_only_name(self):
        return "AAA"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.name} {self.quantity} times
        """

    def __send(self):
        pass
#Abstraction is about hiding complex process that happens in the BG (e.g, sending email)
    def  send_email():
        pass
