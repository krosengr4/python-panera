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


def process_bread_choice():
    user_interface.bread_options()

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