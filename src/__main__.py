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

        prnt(Fore.CYAN, 'Recipe Name:')
        prnt(Fore.BLUE, recipe[0], '\n')

        prnt(Fore.CYAN, 'Author Name:')
        prnt(Fore.BLUE, recipe[1], '\n')

        prnt(Fore.CYAN, 'Ingredients:')
        for element in recipe[2]:
            prnt(Fore.BLUE, element)

        print('')

        prnt(Fore.CYAN, 'Preparation:')
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


#
# def search_recipe():
#     user_string = str(input('What are you looking for? '))
#     if user_string == "pasta" or "Pasta":
#         print("hello")
#
#
# def favorite_recipe(fav_recipe):
#     return fav_recipe
#

def main_menu():
    print("""RECIPE REALM
    1. Search Recipes   -- type 'search' to search the recipes
    2. List Recipes     -- type 'list' to list down the recipes
    3. Create Recipes   -- type 'create' to create the recipes
    4. Favorite Recipes -- type 'favorite' to heart the recipes
    """)

    while True:

        user_option = input('select your option: ')  ## Input will always be str by default

        if user_option == '1':
            list_down_recipe()
            break

        elif user_option == '2':
            create_recipe()
            break
        else:
            print("Invalid option. Exiting.")

    # elif user_option == '3':
    #     search_recipe()
    #
    # elif user_option == '4':
    #     favorite_recipe()


if __name__ == "__main__":
    # welcome()
    # main_menu()

    list_down_recipe()
    # data = [
    #     ['Biryani', json.dumps({
    #         'ingredients': ['Rice', 'Chawal', 'Oil'],
    #         'method': ['Rice', 'Chawal', 'Oil']
    #     })],
    #     ['Hira', 27, 'Expert programmer']
    # ]
    # db.insert_data('abc', data)
    # print(db.get_data('abc'))
