# Basics Of OOP
# Create a class, functions created as is are called functions
# Functions created in a class are called methods
class Item:
    def calculate_total_price(self, x, y):
        total_price = x*y
        return total_price

item1 = Item() #Creating an instance of class item1
item1.name = "Phone" #assiging item1 some attributes
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name ="Laptop"
item2.price = 1000
item2.quantity = 3

#i changed this comment