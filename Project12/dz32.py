class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions
    def __str__(self):
        return f'{self.name}, price: {self.price}'
class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
    def __str__(self):
        return f'{self.name} {self.surname}'
class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0
    def add_item(self, item, cnt):
        self.products[item] = cnt
    def __str__(self):
        items_str = '\n'.join([f'{item.name}: {self.products[item]} pcs.' for item in self.products])
        return f'User: {self.user}\nItems:\n{items_str}'
    def get_total(self):
        for item in self.products:
            self.total += item.price * self.products[item]
        return self.total
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert cart.get_total() == 60
print(cart.get_total())