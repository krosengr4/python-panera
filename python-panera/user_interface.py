def main_menu():
    print('\n\t-----MAIN MENU------')
    print("""
            ---OPTIONS---
        1 - Order
        2 - Admin
        
        0 - Exit
          """)
    
    return int(input('Enter your option:\n'))

def order_screen():
    print('\n\t-----ORDER------')
    print("""
            ---OPTIONS---
        1 - Order Sandwich
        2 - Order Chips
        3 - Order Drink
        4 - Checkout
        
        0 - Cancel
          """)
    
    return int(input('Enter your option:\n'))
