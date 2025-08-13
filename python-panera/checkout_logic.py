from order import Order

def process_checkout(order):

    order.calculate_total()
    order.print_order()

    input('Press enter to continue')