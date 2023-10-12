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


def main_menu():
    print("""RECIPE REALM
    1. Search Recipes   -- type 'search' to search the recipes
    2. List Recipes     -- type 'list' to list down the recipes
    3. Create Recipes   -- type 'create' to create the recipes
    4. Favorite Recipes -- type 'favorite' to heart the recipes
    """)
    user_option = input('select your option: ')

main_menu()