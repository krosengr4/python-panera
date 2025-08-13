class MenuItem:
    def __init__(self, name):
        self.name = name

class Sandwich(MenuItem):
    def __init__(self, name, size, bread, meat, cheese, extra_meat, extra_cheese, is_toasted):
        super().__init__(name)
        self.size = size
        self.bread = bread
        self.meat = meat 
        self.cheese = cheese 
        self.extra_meat = extra_meat
        self.extra_cheese = extra_cheese
        self.is_toasted = is_toasted
        self.toppings = []
        self.sauces = []

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)

    def add_sauces(self, new_sauce):
        self.sauces.append(new_sauce) 

    def calculate_price(self):
        price = 0.0

        if self.size == 'small':
            price += 5.50
        elif self.size == 'medium':
            price += 7.00
        elif self.size == 'large':
            price += 8.50
        
        if self.extra_meat == True:
            price += 1.00

        if self.extra_cheese == True:
            price += 0.75

        if self.is_toasted == True:
            price += 0.50

        return price
    
    def print_data(self):
        print('\t-----SANDWICH-----')
        print('Size:', self.size)
        print('Bread:', self.bread)
        print('Meat:', self.meat)
        if self.extra_meat == True:
            print('Extra meat!')
        print('Cheese:', self.cheese)
        if self.extra_cheese == True:
            print('Extra cheese!')

        if len(self.toppings) == 0:
            print('No toppings')
        else:
            for topping in self.toppings:
                print('Topping:', topping)

        if len(self.sauces) == 0:
            print('No sauce')
        else:
            for sauce in self.sauces:
                print('Sauce:', sauce)
        
        if self.is_toasted == True:
            print('Toasted!')
        else:
            print('Not toasted')
            
        price = self.calculate_price()
        print('Price: $' + price)
        print('------------------------------')
            

class Chip(MenuItem):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def calculate_price():
        return 2.25
    
    def print_data(self):
        print('\t-----CHIP-----')
        print('Type:', self.type)
        price = self.calculate_price()
        print('Price: $' + price)
        print('------------------------------')

    
class Drink(MenuItem):
    def __init__(self, name, type, size):
        super().__init__(name)
        self.type = type
        self.size = size
    
    def calculate_price(self):
        if self.size == 'small':
            return 0.80
        elif self.size == 'medium':
            return 1.25
        elif self.size == 'large':
            return 2.00
        
    def print_data(self):
        print('\t-----DRINK-----')
        print('Type:', self.type)
        print('Size:', self.size)
        price = self.calculate_price()
        print('Price: $' + price)
        print('------------------------------')
