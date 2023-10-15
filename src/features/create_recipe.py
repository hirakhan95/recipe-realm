from src.utils import Fore, prnt, inpt, prnt_new_page
from src.globals import RECIPES, USER_NAME


def create_recipe():
    """ For Recipe Name """
    while True:
        prnt_new_page()
        recipe_name = inpt(Fore.GREEN, 'Enter Recipe Name: ')
        if recipe_name not in [row[0] for row in RECIPES]:
            print('Thank you. Enter ingredients with correct measurements. Press Enter when done!')
            break
        else:
            print('Recipe already exists! Enter Recipe Name Again. ')

    """ For Ingredients """
    ingredients_list = []
    index = 1
    while True:
        ingredient_input = input(f'Enter Ingredient {index} or r/R to end: ')
        index += 1

        if ingredient_input == 'r' or ingredient_input == 'R':
            break

        ingredients_list.append(ingredient_input)

    """ 
    For Preparation
    """
    print('Enter Preparation method. Press Enter when done!')
    preparation_list = []
    index = 1
    while True:
        preparation_input = input(f'Enter Preparation step {index} or r/R to end: ')
        index += 1

        if preparation_input == 'r' or preparation_input == 'R':
            break

        preparation_list.append(preparation_input)

    list_to_insert = [recipe_name, USER_NAME, ingredients_list, preparation_list]
    RECIPES.append(list_to_insert)
    print('Updating database...')
    db.insert_data('recipes', RECIPES)