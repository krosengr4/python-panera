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
                bread = 'white'
                if_continue = False
            case 2:
                bread = 'wheat'
                if_continue = False
            case 3:
                bread = 'rye'
                if_continue = False
            case 4:
                bread = 'sourdough'
                if_continue = False
            case _:
                print('Please choose one of the options that are listed!!!')

    return bread

def process_meat():
    print('Meat')

def process_cheese():
    print('Cheese')

def process_toppings():
    print('Toppings')

def process_sauces():
    print('Sauces')

def process_toasted():
    print('Toasted or not')