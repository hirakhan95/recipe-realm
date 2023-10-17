import src.sheet_db as db
from src.utils import Fore, prnt, inpt, prnt_new_page, prnt_with_columns


def update_single_recipe(recipe, state_variables) -> list:
    wrong_answer = False

    while True:
        prnt_new_page(username=state_variables.USER_NAME)
        prnt(Fore.CYAN, f'UPDATE "{recipe[0]}" RECIPE!\n')

        prnt(Fore.BLUE, 'What do you want to update?\n'
                        '1.Recipe Name\n2.Ingredients\n3.Preparation')
        print()
        prnt(Fore.LIGHTYELLOW_EX, 's/S to save the changes: ')

        user_input = inpt(Fore.GREEN, 'Select what you want to update: ')
        print()

        if wrong_answer:
            prnt(Fore.RED, 'Wrong selection')

        # s/S to go back to the main menu
        if user_input == 's' or user_input == 'S':
            return recipe

        try:
            # converting user input into integer
            user_input = int(user_input)

            # validating if the user input is within the list
            if user_input in [1, 2, 3]:

                if user_input == 1:
                    update_recipe_name = input('Enter new recipe name:')
                    recipe[0] = update_recipe_name

                if user_input == 2:
                    ingredients_list = []
                    while True:
                        update_ingredients_name = input('Enter updated ingredients or r/R to return: ')
                        if update_ingredients_name == 'r' or update_ingredients_name == 'R':
                            break
                        ingredients_list.append(update_ingredients_name)

                    recipe[2] = ingredients_list

                if user_input == 3:
                    preparation_list = []
                    while True:
                        update_prep_name = input('Enter updated preparation or R to return: ')
                        if update_prep_name == 'r' or update_prep_name == 'R':
                            break
                        preparation_list.append(update_prep_name)
                    recipe[3] = preparation_list

                wrong_answer = False

            else:
                wrong_answer = True

        except ValueError as e:
            wrong_answer = True

    return recipe


def update_recipe(state_variables):
    wrong_answer = False
    unauthorize = False

    while True:
        prnt_new_page(username=state_variables.USER_NAME)
        prnt(Fore.CYAN, 'UPDATE RECIPES!\n')

        prnt_with_columns([i[0] for i in state_variables.RECIPES])
        print()

        prnt(Fore.LIGHTYELLOW_EX, 'Press r/R to return\n')

        if wrong_answer:
            prnt(Fore.RED, 'Wrong selection')

        if unauthorize:
            prnt(Fore.RED, 'You are not authorized to do that!')

        user_input = inpt(Fore.GREEN, 'Select a recipe to update: ')

        # r/R to go back to the main menu
        if user_input == 'r' or user_input == 'R':
            return

        try:
            # converting user input into integer
            user_input = int(user_input)

            # validating if the user input is within the list
            if user_input >= 0 and user_input < len(state_variables.RECIPES):

                # Checks if user name matches author name or if it is admin
                # If it is not do not delete
                if state_variables.USER_NAME == state_variables.RECIPES[user_input][
                    1] or state_variables.USER_NAME == 'admin':

                    recipe = update_single_recipe(state_variables.RECIPES[user_input], state_variables)
                    state_variables.RECIPES[user_input] = recipe
                    print()
                    prnt(Fore.LIGHTYELLOW_EX, 'Updating database...')
                    db.insert_data('recipes', state_variables.RECIPES)

                    wrong_answer = False
                    unauthorize = False

                else:
                    wrong_answer = False
                    unauthorize = True

            else:
                wrong_answer = True
                unauthorize = False

        except ValueError as e:
            wrong_answer = True
            unauthorize = False
