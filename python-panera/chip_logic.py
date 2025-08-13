import user_interface
from order import Order
from menu_item import Chip

def process_add_chips(order):
    user_choice = user_interface.chip_options()
    chip_type = ''

    match user_choice:
        case 1:
            chip_type = 'Original Potato Chips'
        case 2:
            chip_type = 'Jalepeno'
        case 3:
            chip_type = 'Sea Salt and Vinegar'
        case 4:
            chip_type = 'Barbeque'
        case 5: 
            chip_type = 'Harvest Cheddar'
        case _:
            print('Please enter a valid option!')

    add_to_order(chip_type, order)

def add_to_order(chip_type, order):
    chip = Chip('Chips', chip_type)

    order.add_item(chip)

