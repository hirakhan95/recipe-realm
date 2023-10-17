import os
import platform
from colorama import Fore, init


def prnt(color, *args, **kwargs):
    print(color, *args, **kwargs, sep='')


def inpt(color: Fore, *args, **kwargs):
    print(color)
    return input(*args, **kwargs)


def prnt_new_page():
    if platform.system() == 'Windows':
        os.system('cls')
        print(platform.system())
    else:
        os.system('clear')
        print(platform.system())

    print('something')

    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#', ' ' * 76, '#')
    print(Fore.YELLOW + '#', ' ' * 31, 'RECIPE REALM', ' ' * 31, '#')
    print(Fore.YELLOW + '#', ' ' * 76, '#')
    print(Fore.YELLOW + '#' * 80)
    print(Fore.YELLOW + '#' * 80)
    print('\n')
