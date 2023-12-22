class Item:
    def __init__(self, name: str, price: float, quantity=0):

        #Run argument to assignment
        assert price >= 0, f"Price {price} not valid"
        assert quantity >= 0

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return print(self.price*self.quantity)  


item1 = Item("Phone" , -1, 100)
# item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item('Laptop', 1000, 3)
# item2.calculate_total_price()
# print(item1.name)
# print(item2.name)
# print(item1.quantity)
# print(item2.quantity)

