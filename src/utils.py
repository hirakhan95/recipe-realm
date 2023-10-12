from colorama import Fore


def prnt(color, *args, **kwargs):
    print(color, *args, **kwargs, sep='')


def inpt(color: Fore, *args, **kwargs):
    print(color)
    return input(*args, **kwargs)
