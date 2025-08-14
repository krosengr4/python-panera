import user_interface
from menu_item import Sandwich
from order import Order

def process_make_sandwich(order):
    print('Make a new sandwich')

def process_size():
    if_continue = True

    while if_continue:
        size_choice = user_interface.sandwich_sizes()
        match size_choice:
            case 1:
                size = 'small'
                if_continue = False
            case 2:
                size = 'medium'
                if_continue = False
            case 3:
                size = 'large'
                if_continue = False
            case _:
                print('Please enter a valid option!!!')
    
    return size


def process_bread_choice():
    if_continue = True

    while if_continue:
        bread_choice = user_interface.bread_options()

        match bread_choice:
            case 1:
                bread = 'White'
                if_continue = False
            case 2:
                bread = 'Wheat'
                if_continue = False
            case 3:
                bread = 'Rye'
                if_continue = False
            case 4:
                bread = 'Sourdough'
                if_continue = False
            case _:
                print('Please choose one of the options that are listed!!!')

    return bread

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
    print('Toppings')

def process_sauces():
    print('Sauces')

def process_toasted():
    print('Toasted or not')