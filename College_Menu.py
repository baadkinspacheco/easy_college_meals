# Cheap and easy meals for the average college student

def menu():
    med_chicken = {'chicken', 'olives', 'butter', 'olive oil', 'white wine', 'capers', 'tomatos', 'salt', 'pepper', 'pan'}
    pasta = {'pasta', 'tomato sauce', 'pot'}
    chicken_tacos = {'tortilla', 'salsa', 'cilantro', 'lime', 'chicken', 'cheese', 'beans', 'avocado', 'pan'}
    # Don't see anything you like??
    # Randomly generate a meal with lists of ingredients from menu items

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

    # Create a new menu item



main()
