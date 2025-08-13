import user_interface

def process_add_drink(order):
    print('drink')

def drink_type():

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