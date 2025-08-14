def main_menu():
    print('\n\t-----MAIN MENU------')
    print("""
            ---OPTIONS---
        1 - Order
        
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

def sandwich_sizes():
    print('\n\t-----CHOOSE YOUR SIZE------')
    print("""
                    ---SIZES---
        1 - Small (4")...           $5.50
        2 - Medium (8")...          $7.00
        3 - Large (12")...          $8.50
          """)
    
    return int(input('Enter your option:\n'))

def bread_options():
    print('\n\t-----CHOOSE YOUR BREAD------')
    print("""
            ---OPTIONS---
        1 - White
        2 - Wheat
        3 - Rye
        4 - Sourdough
          """)
    
    return int(input('Enter your option:\n'))

def meat_options():
    print('\n\t-----CHOOSE YOUR MEAT------')
    print("""
            ---OPTIONS---
        1 - Steak
        2 - Ham
        3 - Turkey
        4 - Chicken
        5 - No meat
          """)
    
    return int(input('Enter your option:\n'))

def extra_meat_option():
    print('\n\t-----WOULD YOU LIKE EXTRA MEAT?-----')
    print("""
            ---OPTIONS---
          1 - Yes ($1.00)
          2 - No
          """)
    
    return int(input('Enter your option:\n'))

def cheese_options():
    print('\n\t-----CHOOSE YOUR CHEESE-----')
    print("""
            ---OPTIONS---
        1 - American
        2 - Provolone
        3 - Cheddar
        4 - Swiss
        5 - No cheese
          """)
    
    return int(input('Enter your option:\n'))

def extra_cheese_option():
    print('\n\t-----WOULD YOU LIKE EXTRA CHEESE?-----')
    print("""
            ---OPTIONS---
          1 - Yes ($0.75)
          2 - No
          """)
    
    return int(input('Enter your option:\n'))

def toppings_options():
    print('\n\t-----CHOOSE YOUR TOPPINGS-----')
    print("""
                    ---OPTIONS---
            1 - Lettuce         6 - Cucumbers             
            2 - Peppers         7 - Pickles
            3 - Onions          8 - Guacamole
            4 - Tomatoes        9 - Mushrooms
            5 - Jalepenos       0 - No Toppings     
          """)
    
    return int(input('Enter your option:\n'))

def sauce_options():
    print('\n\t-----CHOOSE YOUR SAUCE-----')
    print("""
                        ---OPTIONS---
            1 - Mayo                5 - Vinnigrette                              
            2 - Mustard             6 - Au Jus
            3 - Ketchup             7 - Barbeque 
            4 - Thousand Islands    8 - Relish 
          """)
    
    return int(input('Enter your option:\n'))

def toasted_option():
    print('\n\t-----WOULD YOU LIKE YOUR SANDWICH TOASTED?-----')
    print("""
            ---OPTIONS---
          1 - Yes ($0.50)
          2 - No
          """)
    
    return int(input('Enter your option:\n'))

def chip_options():
    print('\n\t-----CHOOSE YOUR CHIP-----')
    print('\tAll chips are $2.25')
    print("""
                ---OPTIONS---
          1 - Original Potato Chips
          2 - Jalepeno
          3 - Sea Salt and Vinegar
          4 - Barbeque
          5 - Harvest Cheddar
          """)
    
    return int(input('Enter your option:\n'))

def drink_opitons():
    print('\n\t-----CHOOSE YOUR DRINK-----')
    print("""
                ---OPTIONS---
          1 - Fountain Drink
          2 - Lemonade
          3 - Milkshake
          4 - Sweet Tea
          5 - Unsweet Tea
          """)
    
    return int(input('Enter your option:\n'))

def drink_sizes():
    print('\n\t-----CHOOSE YOUR DRINK SIZE-----')
    print("""
                        ---SIZES---
          1 - Small (12oz)...           $0.80
          2 - Medium (16oz)...          $1.25
          3 - Large (24oz)...           $2.00
          """)
    
    return int(input('Enter your option:\n'))