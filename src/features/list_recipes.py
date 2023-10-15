from src.utils import Fore, prnt, inpt, prnt_new_page
from src.globals import RECIPES


def print_recipe(n):
    """

    :param n: list
    :return: string
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
