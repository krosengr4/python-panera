from order import Order

def process_checkout(order):

    order.calculate_total()
    order.print_order()

    user_confirm = input("""
                         
                            ---IS THIS ORDER CORRECT?---
                         1 - Yes                    2 - No

                         """).lower()
    
    if user_confirm == '1':
        print('Sweet! Your food will be out to you shortly!!!\n')
    elif user_confirm == '2':
        print('Oh no... Lets try again!\n')

    order.clear_order()
    input('Press enter to continue...')