import user_interface

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
    user_interface.order_screen()