import user_interface
from menu_item import Sandwich
from order import Order

def process_make_sandwich(order):
    size = process_size()
    bread = process_bread_choice()
    meat = process_meat()
    extra_meat = process_extra_meat()
    cheese = process_cheese()
    extra_cheese = process_extra_cheese()
    toppings = process_toppings()
    sauces = process_sauces()
    is_toasted = process_toasted()

    new_sandwich = Sandwich('Sandwich', size, bread, meat, cheese, extra_meat, extra_cheese, is_toasted)
    for topping in toppings:
        new_sandwich.add_topping(topping)
    for sauce in sauces:
        new_sandwich.add_sauces(sauce)

    order.add_item(new_sandwich)

def process_size():
    while True:
        size_choice = user_interface.sandwich_sizes()
        match size_choice:
            case 1:
                return 'small'
            case 2:
                return 'medium'
            case 3:
                return 'large'
            case _:
                print('Please enter a valid option!!!')


def process_bread_choice():
    while True:
        bread_choice = user_interface.bread_options()

        match bread_choice:
            case 1:
                return 'White'
            case 2:
                return 'Wheat'
            case 3:
                return 'Rye'
            case 4:
                return 'Sourdough'
            case _:
                print('Please choose one of the options that are listed!!!')

def process_meat():
    while True:
        meat_choice = user_interface.meat_options()

        match meat_choice:
            case 1:
                return 'Steak'
            case 2:
                return 'Ham'
            case 3:
                return 'Turkey'
            case 4:
                return 'Chicken'
            case 5:
                return 'None'
            case _:
                print('Please enter a valid option!!!')

def process_extra_meat():
    while True:
        extra_meat = user_interface.extra_meat_option()

        if extra_meat == 1:
            return True
        elif extra_meat == 2:
            return False
        else:
            print("Please enter a valid option!!!")


def process_cheese():
    while True:
        cheese_option = user_interface.cheese_options()

        match cheese_option:
            case 1:
                return 'American'
            case 2:
                return 'Provolone'
            case 3:
                return 'Cheddar'
            case 4:
                return 'Swiss'
            case 5:
                return 'None'
            case _:
                print('Please enter a valid option!!!')

def process_extra_cheese():
    while True:
        extra_cheese = user_interface.extra_cheese_option()

        if extra_cheese == 1:
            return True
        elif extra_cheese == 2:
            return False
        else:
            print('Please enter a valid option!!!')

def process_toppings():
    toppings = []
    
    while True:
        toppings_choice = user_interface.toppings_options()

        match toppings_choice:
            case 1:
                toppings.append('Lettuce')
            case 2:
                toppings.append('Peppers')
            case 3:
                toppings.append('Onions')
            case 4:
                toppings.append('Tomatoes')
            case 5:
                toppings.append('Jalepenos')
            case 6:
                toppings.append('Cucumbers')
            case 7:
                toppings.append('Pickles')
            case 8:
                toppings.append('Guacomole')
            case 9:
                toppings.append('Mushrooms')
            case 0:
                toppings.clear()
                toppings.append('None')
            case _:
                print('Please enter a valid option!!!')
            
        add_more = int(input("Would you like to add more?\n1 - Yes\n2 - No\nEnter here: "))
                       
        if add_more == 2:
            return toppings
        elif add_more != 1:
            print('Please enter either 1 or 2!!!')
                                 

def process_sauces():
    sauces = []

    while True:
        sauce_choice = user_interface.sauce_options()

        match sauce_choice:
            case 1:
                sauces.append('Mayo')
            case 2:
                sauces.append('Mustard')
            case 3:
                sauces.append('Ketchup')
            case 4:
                sauces.append('Thousand Island')
            case 5:
                sauces.append('Vinaigrette')
            case 6:
                sauces.append('Au Jus')
            case 7:
                sauces.append('Barbeque')
            case 8:
                sauces.append('Relish')
            case 0:
                sauces.clear()
                sauces.append('None')
            case _:
                print('Please enter a valid option!!!')

        add_more = int(input("Would you like to add more?\n1 - Yes\n2 - No\nEnter here: "))

        if add_more == 2:
            return sauces
        elif add_more != 1:
            print('Please enter either 1 or 2!')
                

def process_toasted():
    while True:
        toasted_option = user_interface.toasted_option()

        if toasted_option == 1:
            return True
        elif toasted_option == 2:
            return False
        else:
            print('Please enter a valid option!!!')