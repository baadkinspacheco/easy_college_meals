'''     Author: Brooke Adkins
        Description: Cheap and easy meals for the average college student.
        Also includes feature where tasks can be prioritzed during cooking time.
'''

def menu():
    menu = {'chicken dinner': {'chicken', 'olives', 'butter', 'olive oil', 'white wine', 'capers', 'tomatos', 'salt', 'pepper'},
    'pasta': {'pasta', 'tomato sauce', 'pot'}, 'chicken tacos': {'tortilla', 'salsa', 'cilantro', 'lime', 'chicken', 'cheese', 'beans', 'avocado'}}
    return menu
    # Don't see anything you like??
    # Randomly generate a meal with lists of ingredients from menu items

def cook_time():
    cook_time =  {'chicken dinner': 30, 'pasta': 10, 'chicken tacos': 20}
    return cook_time

def add_menu_item(menu):
    meal = input('What is the name of this meal?\n')
    time = input('How long does it take to prepare and cook?\n')
    print('What are the ingredients? Hit return after each item.')
    ingredients = items()
    menu[meal] = ingredients
    time[meal] = time

def items():
    """ Returns a set of items the user
    has in their kitchen.
    """
    items = set()
    condition = True
    while condition == True:
        add_item = input()
        if add_item.lower() == 'none':
            condition == False
            break
        items.add(add_item.strip())
    return items

def main():
    # Create list of ingredients
    print('What is in your refrigerator and pantry? Print \'None\' when there is nothing else to add.')
    ingredients = items()
    print(ingredients)

    # Creates list of spices
    print('What spices do you have? Print \'None\' when there is nothing else to add.')
    spices = items()
    print(spices)

    # Create list of supplies
    print('What dishes are clean?  Print \'None\' when there is nothing else to add.')
    supplies = items()
    print(supplies)

    # How much time do you have
    time = input('How much time do you have?\n')

    # Do you want to complete other tasks while its cooking?
    other_task = input('Do you want to complete other tasks while it cooks?\n')
    # if no don't continue, if yes ask how long will it take you to sweep...other chores
    # then makes a list of to do so you can stay productive and keep a clean space

    # What menu items would you liek to cook in the furture?
    # From list of menu items create a shopping list
    menu = menu()

    # Create a new menu item
    while True:
        command = input('Would you like to add an item to the menu? Reply yes or no')
        if command.lower() == 'yes':
            add_menu_item(menu)
        elif command.lower() == 'no':
            break
        else:
            print('Please type in \'yes\' or \'no\'')


main()
