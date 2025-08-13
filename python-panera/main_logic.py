import user_interface, sandwich_logic, chip_logic, drink_logic, checkout_logic
from order import Order

def process_main_menu():

    if_continue = True

    while if_continue:
        user_choice = user_interface.main_menu()

        match user_choice:
            case 1:
                process_order_screen()
            case 0:
                if_continue = False
            case _:
                print('Please enter a valid option!')

def process_order_screen():

    customer_name = input('Please enter a name for the order:\n')
    order = Order(customer_name)

    if_continue = True

    while if_continue:
        user_choice = user_interface.order_screen()

        match user_choice:
            case 1:
                sandwich_logic.process_make_sandwich(order)
            case 2:
                chip_logic.process_add_chips(order)
            case 3:
                drink_logic.process_add_drink(order)
            case 4: 
                checkout_logic.process_checkout(order)
            case 0:
                if_continue = False
            case _:
                print('Please enter a valid option!')