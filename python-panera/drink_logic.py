import user_interface
from menu_item import Drink
from order import Order

def process_add_drink(order):
    drink_choice = select_drink_type()
    drink_size = select_drink_size()

    new_drink = Drink('Drink', drink_choice, drink_size)
    order.add_item(new_drink)

def select_drink_type():
    while True:
        user_choice = user_interface.drink_opitons()

        match user_choice:
            case 1:
                return 'Fountain Drink'
            case 2:
                return 'Lemonade'
            case 3:
                return 'Milkshake'
            case 4:
                return 'Sweet Tea'
            case 5:
                return 'Unsweet Tea'
            case _:
                print('Please enter a valid option!')

def select_drink_size():
    while True:
        user_choice = user_interface.drink_sizes()

        match user_choice:
            case 1:
                return 'small'
            case 2:
                return 'medium'
            case 3:
                return 'large'
            case _:
                print('Please enter a valid option!!!')
