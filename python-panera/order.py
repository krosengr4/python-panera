from menu_item import Sandwich, Chip, Drink

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)
    
    def calculate_total(self):
        price = 0.0

        for item in self.items:
            price += item.calculate_price()

        return price
    
    def print_order(self):
        print('-----ORDER FOR', self.customer_name.upper() + '-----\n')

        for item in self.items:
            item.print_data()

        print(f'Total price: ${self.calculate_total():,.2f}')
    
