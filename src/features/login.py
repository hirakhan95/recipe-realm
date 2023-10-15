from src.utils import Fore, prnt, inpt, prnt_new_page
from src.globals import USER_NAME, ADMIN_PASSWORD


def login():
    global USER_NAME

    USER_NAME = inpt(Fore.GREEN, 'Hey there! Enter your name: ')

    while USER_NAME == 'admin':
        password = inpt(Fore.GREEN, 'Enter Admin Password: ')
        if password == ADMIN_PASSWORD:
            break
        prnt(Fore.RED, 'Incorrect Password!')

    prnt(Fore.MAGENTA, f"Welcome, {USER_NAME} to the Recipe Realm!\nWhere Flavors Find a Home :)")