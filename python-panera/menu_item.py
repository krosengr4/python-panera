class MenuItem:
    def __init__(self, name):
        self.name = name

class Sandwich(MenuItem):
    def __init__(self, name, size, bread, meat, cheese, is_toasted):
        super().__init__(name)
        self.size = size
        self.bread = bread
        self.meat = meat 
        self.cheese = cheese 
        self.is_toasted = is_toasted
        self.toppings = []
        self.sauces = [] 

    def calculate_price():
        if