import os
from colorama import Fore, init


def prnt(color, *args, **kwargs):
    print(color, *args, **kwargs, sep='')


def inpt(color: Fore, *args, **kwargs):
    print(color)
    return input(*args, **kwargs)


def prnt_new_page():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the header
    print('\n'*200)
    print(os.name)
    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#', ' ' * 76, '#')
    print(Fore.YELLOW + '#', ' ' * 31, 'RECIPE REALM', ' ' * 31, '#')
    print(Fore.YELLOW + '#', ' ' * 76, '#')
    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#' * 80)
    print('\n')
