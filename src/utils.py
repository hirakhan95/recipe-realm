import os
import math
from colorama import Fore


def prnt(color, *args, **kwargs):
    print(color, *args, **kwargs, sep='')


def inpt(color: Fore, *args, **kwargs):
    print(color)
    return input(*args, **kwargs)


def prnt_new_page(color=Fore.YELLOW, username=None):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(color + '#' * 80)
    print(color + '#' * 80)
    print(color + '#', ' ' * 76, '#')
    print(color + '#', ' ' * 31, 'RECIPE REALM', ' ' * 31, '#')

    if username:
        text = f"User: {username}"
        print(color + '#', text.center(76), '#')

    print(color + '#', ' ' * 76, '#')
    print(color + '#' * 80)
    print(color + '#' * 80)
    print('\n')


def prnt_with_columns(data, color=Fore.BLUE, columns=3):
    rows = math.ceil(len(data) / columns)

    i = 0
    for row in range(rows):
        temp = []
        for j in range(columns):
            if i < len(data):
                temp.append(f"{i: 3d} {data[i]: <23}")
                i += 1
        prnt(color, *temp)
