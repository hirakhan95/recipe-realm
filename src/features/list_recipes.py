from src.utils import Fore, prnt, inpt, prnt_new_page, prnt_with_columns


def print_recipe(state_variables, n):
    recipe = state_variables.RECIPES[n]
    is_wrong = False

    # start a while loop
    while True:

        # print Recipe name, Author name, Ingredients, Preparation
        prnt_new_page(username=state_variables.USER_NAME)

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
        user_input = inpt(Fore.GREEN, 'Enter r/R to return: ')
        if user_input == 'r' or user_input == 'R':
            return

        is_wrong = True


def list_down_recipe(state_variables):
    is_wrong = False

    while True:
        prnt_new_page(username=state_variables.USER_NAME)
        #
        prnt(Fore.CYAN, 'HERE ARE THE RECIPES!\n')

        prnt_with_columns([i[0] for i in state_variables.RECIPES])
        print()
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
            if 0 <= user_input < len(state_variables.RECIPES):
                print_recipe(state_variables, user_input)
                is_wrong = False

            else:
                is_wrong = True
        except ValueError as _:
            is_wrong = True
