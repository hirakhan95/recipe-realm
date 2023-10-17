import src.sheet_db as db
from src.utils import Fore, prnt, inpt, prnt_new_page, prnt_with_columns


def delete_recipe(state_variables):
    wrong_answer = False
    unauthorize = False

    while True:
        prnt_new_page(username=state_variables.USER_NAME)
        prnt(Fore.CYAN, 'DELETE RECIPES!\n')

        prnt_with_columns([i[0] for i in state_variables.RECIPES])
        print()

        prnt(Fore.LIGHTYELLOW_EX, 'Press r/R to return\n')

        if wrong_answer:
            prnt(Fore.RED, 'Wrong selection')

        if unauthorize:
            prnt(Fore.RED, 'You are not authorized to do that!')

        user_input = inpt(Fore.GREEN, 'Provide response: ')

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
                    del state_variables.RECIPES[user_input]
                    print()
                    prnt(Fore.LIGHTYELLOW_EX, 'Updating database...')
                    db.insert_data('recipes',
                                   state_variables.RECIPES)  # Remove for Explicit save functionality
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
