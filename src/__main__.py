import src.sheet_db as db
from src.utils import Fore, prnt, inpt, prnt_new_page

RECIPES = db.get_data('recipes')
USER_NAME = None
ADMIN_PASSWORD = 'RecipeRealm'


def login():
    global USER_NAME
    USER_NAME = inpt(Fore.GREEN, 'Hey there! Enter your name: ')

    while USER_NAME == 'admin':
        password = inpt(Fore.GREEN, 'Enter Admin Password: ')
        if password == ADMIN_PASSWORD:
            break
        prnt(Fore.RED, 'Incorrect Password!')

    prnt(Fore.MAGENTA, f"Welcome, {USER_NAME} to the Recipe Realm!\nWhere Flavors Find a Home :)")


def create_recipe():
    """ For Ingredients
    """
    print('Enter ingredients with correct measurements. Type "done" when done!')
    string_list = []
    while True:
        ingredients = str(input())
        string_list.append(ingredients)

        if ingredients == 'done':
            break
        list_of_ingredients = ' \n'.join(string_list)

    """ For Preparation
    """
    print('Enter Preparation method. Press Enter when done!')
    method_list = []
    while True:
        preparation = str(input())
        method_list.append(preparation)

        if preparation == '':
            break
        method_description = ' \n'.join(method_list)

    print(f'INGREDIENTS:\n{list_of_ingredients}\n')
    print(f'PREPARATION:\n{method_description}')


def print_recipe(n):
    """

    :param n: list
    :return: sring
    """
    recipe = RECIPES[n]
    is_wrong = False

    # start a while loop
    while True:

        # print Recipe name, Author name, Ingredients, Preparation
        prnt_new_page()

        prnt(Fore.CYAN, f'{recipe[0]} Recipe')
        print('')

        prnt(Fore.MAGENTA, 'Author Name:')
        prnt(Fore.BLUE, recipe[1], '\n')

        prnt(Fore.MAGENTA, 'Ingredients:')
        for element in recipe[2]:
            prnt(Fore.BLUE, element)

        print('')

        prnt(Fore.MAGENTA, 'Preparation:')
        for element in recipe[3]:
            prnt(Fore.BLUE, element)

        if is_wrong:
            prnt(Fore.RED, '\n', 'Wrong selection')

        # take an input from user r or R to exit from function
        user_input = inpt(Fore.GREEN, 'Enter r\R to return: ')
        if user_input == 'r' or user_input == 'R':
            return

        is_wrong = True


def list_down_recipe():
    is_wrong = False

    while True:
        prnt_new_page()
        #
        prnt(Fore.CYAN, 'HERE ARE THE RECIPES!\n')
        for index, row in enumerate(RECIPES):
            prnt(Fore.BLUE, index, ' ', row[0])
        prnt(Fore.LIGHTYELLOW_EX, 'Press r/R to return\n')

        # if the selection is wrong
        if is_wrong:
            prnt(Fore.RED, 'Wrong selection')

        # user response
        user_input = str(inpt(Fore.GREEN, 'Provide response: '))

        #
        if user_input == 'r' or user_input == 'R':
            return

        try:
            # Converting user input into integer
            user_input = int(user_input)

            # Validating if the user input is within the selection
            if user_input >= 0 and user_input < len(RECIPES):
                print_recipe(user_input)
                is_wrong = False

            else:
                is_wrong = True
        except ValueError as e:
            is_wrong = True


def search_recipe():
    # user_string = str(input('What are you looking for? '))
    # if user_string == "pasta" or "Pasta":
    #     print("hello")
    pass


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
                        "2. Create Recipes\n"
                        "3. Search Recipes\n"
                        "4. Delete Recipes")

        prnt(Fore.CYAN, "Press s/S to Save All")

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
            search_recipe()

        elif user_option == '4':
            delete_recipe()

        elif user_option == 's' or user_option == 'S':
            save_recipe()

        else:
            wrong_answer = True


def save_recipe():
    db.insert_data('recipes', RECIPES)


def delete_recipe():
    wrong_answer = False
    unauthorize = False

    while True:
        prnt_new_page()
        prnt(Fore.MAGENTA, 'DELETE RECIPES!\n')
        for index, value in enumerate(RECIPES):
            prnt(Fore.BLUE, index, ' ', value[0])

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
            if user_input >= 0 and user_input < len(RECIPES):

                # Checks if user name matches author name or if it is admin
                # If it is not do not delete

                if USER_NAME == value[1] or USER_NAME == 'admin':
                    del RECIPES[user_input]
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


if __name__ == "__main__":
    login()
    main_menu()
