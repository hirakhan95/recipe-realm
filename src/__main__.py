import src.sheet_db as db
from src.utils import Fore, prnt, inpt, prnt_new_page

from .features import login, list_down_recipe, delete_recipe


RECIPES = db.get_data('recipes')
USER_NAME = None
ADMIN_PASSWORD = 'RecipeRealm'




# Explicit save functionality
# def save_recipe():
#     db.insert_data('recipes', RECIPES)

def main_menu():
    wrong_answer = False
    while True:
        # print new page
        # remove break
        # take input 1 2 3 4 for search, list, create, delete
        # take an input from user r or R to exit from function
        prnt_new_page()
        prnt(Fore.CYAN, 'MAIN MENU')
        print('')
        prnt(Fore.BLUE, "1. List Recipes\n"
                        "2. Create Recipe\n"
                        "3. Update Recipe\n"
                        "4. Delete Recipes")

        # Explicit save functionality
        # prnt(Fore.CYAN, "Press s/S to Save All")

        prnt(Fore.LIGHTYELLOW_EX, 'Press e/E to Exit\n')

        #
        if wrong_answer:
            prnt(Fore.RED, 'Invalid option. Enter number from 1-4')
            wrong_answer = False

        user_option = inpt(Fore.GREEN, 'select your option: ')  ## Input will always be str by default

        if user_option == 'e' or user_option == 'E':
            return

        if user_option == '1':
            list_down_recipe()

        elif user_option == '2':
            create_recipe()

        elif user_option == '3':
            update_recipe()

        elif user_option == '4':
            delete_recipe()

        # Explicit save functionality
        # elif user_option == 's' or user_option == 'S':
        #     save_recipe()

        else:
            wrong_answer = True



if __name__ == "__main__":
    login()
    main_menu()
    # create_recipe()
    # update_recipe()
