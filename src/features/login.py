from src.utils import Fore, prnt, inpt, prnt_new_page


def login(state_variables):
    prnt_new_page()

    prnt(Fore.CYAN, 'Login to Realm!', '\n')

    state_variables.USER_NAME = inpt(Fore.GREEN, 'Hey there! Enter your name: ')

    while state_variables.USER_NAME == 'admin':
        password = inpt(Fore.GREEN, 'Enter Admin Password: ')
        if password == state_variables.ADMIN_PASSWORD:
            break
        prnt(Fore.RED, 'Incorrect Password!')

    prnt(Fore.MAGENTA, f"Welcome, {state_variables.USER_NAME} to the Recipe Realm!\nWhere Flavors Find a Home :)")
