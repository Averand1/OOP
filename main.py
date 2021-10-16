from item import Item

#Problem will be channging returned output of readonlyname function (ln 8)
item1 =  Item("MyItem", 643)

item1.name = "OtherItem" #Try using _ before name if you want to set some value (self.__name = "YourValue")

print(item1.name)


