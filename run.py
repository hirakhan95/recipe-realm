import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('recipe_data')

# recipes = SHEET.worksheet('recipes')
# data = recipes.get_all_values()
# print(data)


def welcome():
    user_name = str(input('Hey there! Enter your name: '))
    print(f"Welcome, {user_name} to the Recipe Realm!\nWhere Flavors Find a Home :)")

welcome()


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


def list_down_recipe(recipe_list):
    return recipe_list


def search_recipe():
    user_string = str(input('What are you looking for? '))
    if user_string == "pasta" or "Pasta":
        print("hello")


def favorite_recipe(fav_recipe):
    return fav_recipe


def main_menu():
    print("""RECIPE REALM
    1. Search Recipes   -- type 'search' to search the recipes
    2. List Recipes     -- type 'list' to list down the recipes
    3. Create Recipes   -- type 'create' to create the recipes
    4. Favorite Recipes -- type 'favorite' to heart the recipes
    """)
    user_option = input('select your option: ')
    if user_option == 'create':
        create_recipe()

    elif user_option == 'list':
        list_down_recipe()

    elif user_option == 'search':
        search_recipe()

    elif user_option == 'favorite' or 'favourite':
        favorite_recipe()


main_menu()