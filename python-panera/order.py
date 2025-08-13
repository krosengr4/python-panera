from menu_item import Sandwich, Chip, Drink

class Order:
    def __init__(self, customer_name, total_price):
        self.customer_name = customer_name
        self.total_price = total_price
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)
    
    def calculate_total(self):
        price = 0.0

        for item in self.items:
            price += item.calculate_price()

        return price
    
    def print_order(self):
        print('\t-----ORDER FOR', self.customer_name.upper())

        for item in self.items:
            item.print_data()

        print('Total price: $' + self.calculate_total())
    
