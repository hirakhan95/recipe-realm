from src.features import list_down_recipe, delete_recipe, create_recipe, update_recipe
from src.utils import Fore, prnt, inpt, prnt_new_page


def main_menu(state_variables):
    wrong_answer = False
    while True:
        # print new page
        # remove break
        # take input 1 2 3 4 for search, list, create, delete
        # take an input from user r or R to exit from function
        prnt_new_page(username=state_variables.USER_NAME)
        prnt(Fore.CYAN, 'MAIN MENU')
        print('')
        prnt(Fore.BLUE, "1. List Recipes\n"
                        "2. Create Recipe\n"
                        "3. Update Recipe\n"
                        "4. Delete Recipe")

        # Explicit save functionality
        # prnt(Fore.CYAN, "Press s/S to Save All")
        print()
        prnt(Fore.LIGHTYELLOW_EX, 'Press e/E to Exit\n')

        #
        if wrong_answer:
            prnt(Fore.RED, 'Invalid option. Enter number from 1-4')
            wrong_answer = False

        user_option = inpt(Fore.GREEN, 'select your option: ')

        if user_option == 'e' or user_option == 'E':
            print()
            prnt(Fore.LIGHTWHITE_EX, 'Thank you for using Recipe Realm! Come back Soon.')
            return

        if user_option == '1':
            list_down_recipe(state_variables)

        elif user_option == '2':
            create_recipe(state_variables)

        elif user_option == '3':
            update_recipe(state_variables)

        elif user_option == '4':
            delete_recipe(state_variables)

        else:
            wrong_answer = True
