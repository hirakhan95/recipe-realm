import src.sheet_db as db
from src.utils import Fore, prnt, inpt, prnt_new_page

RECIPES = db.get_data('recipes')


def welcome():
    user_name = str(input('Hey there! Enter your name: '))
    print(f"Welcome, {user_name} to the Recipe Realm!\nWhere Flavors Find a Home :)")


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

        # print recipe Recipe name, Author name, Ingredients, Preparation
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

        #
        if is_wrong:
            prnt(Fore.RED, 'Wrong selection')

        #
        user_input = str(inpt(Fore.GREEN, 'Provide response: '))

        #
        if user_input == 'r' or user_input == 'R':
            return

        try:
            #
            user_input = int(user_input)

            #
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


def delete_recipe():
    pass


def main_menu():

    wrong_answer = False
    while True:
        # print new page ---done
        # remove break --done
        # @take input 1 2 3 4 for search, list, create, delete -- done
        # take an input from user r or R to exit from function
        prnt_new_page()
        prnt(Fore.CYAN, 'MAIN MENU')
        print('')
        prnt(Fore.BLUE, "1. List Recipes\n2. Create Recipes\n3. Search Recipes\n4. Delete Recipes")

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

        else:
            wrong_answer = True


if __name__ == "__main__":
    # welcome()
    main_menu()
