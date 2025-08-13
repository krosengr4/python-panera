import user_interface
from menu_item import Drink
from order import Order

def process_add_drink(order):
    drink_choice = select_drink_type()
    drink_size = select_drink_size()

    new_drink = Drink('Drink', drink_choice, drink_size)
    order.add_item(new_drink)

def select_drink_type():

    if_continue = True

    while(if_continue):
        user_choice = user_interface.drink_opitons()

        match user_choice:
            case 1:
                drink_choice = 'Fountain Drink'
                if_continue = False
            case 2:
                drink_choice = 'Lemonade'
                if_continue = False
            case 3:
                drink_choice = ' Milkshake'
                if_continue = False
            case 4:
                drink_choice = 'Sweet Tea'
                if_continue = False
            case 5:
                drink_choice = 'Unsweet Tea'
                if_continue = False
            case _:
                print('Please enter a valid option!')

    return drink_choice

def select_drink_size():
    if_continue = True

    while(if_continue):
        user_choice = user_interface.drink_sizes()

        match user_choice:
            case 1:
                drink_size = 'small'
                if_continue = False
            case 2:
                drink_size = 'medium'
                if_continue = False
            case 3:
                drink_size = 'large'
                if_continue = False
            case _:
                print('Please enter a valid option!!!')
            
    return drink_size