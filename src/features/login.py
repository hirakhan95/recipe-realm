from src.utils import Fore, prnt, inpt, prnt_new_page


def login(state_variables):
    prnt_new_page()
    prnt(Fore.CYAN, "Welcome to Recipe Realm! It's the perfect place for everyone who loves food.\n Here, you can find "
                    "new recipes to try or share your own favorite dishes with \nothers. Whether you're a seasoned cook "
                    "or just starting out in the kitchen, Recipe\nRealm is here to help you explore and enjoy the world "
                    "of cooking. Dive in\nandlet's get cooking!",'\n')

    prnt(Fore.LIGHTYELLOW_EX, 'Login to Realm!', '\n')

    state_variables.USER_NAME = inpt(Fore.GREEN, 'Enter Your Name: ')


    while state_variables.USER_NAME == 'admin':
        password = inpt(Fore.GREEN, 'Enter Admin Password: ')
        if password == state_variables.ADMIN_PASSWORD:
            break
        prnt(Fore.RED, 'Incorrect Password!')
