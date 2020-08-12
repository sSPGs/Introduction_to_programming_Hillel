# ## Подключение модулей ##
#
# import string
# import time
# import typing
# # import random
#
# from random import randint as rnd # Из модуля Random импортировать функцию и назвать как я хочу
#
#
# letters = string.ascii_letters
# print(letters)
#
# some_int = rnd(2, 9)
# print(some_int)

def print_my():
    print("Hello, HELLLOOOOOO!!!!!!!!!!")


def print_dict(some_dict, test_value):
    for key in some_dict:
        print(test_value)
        print(f"'{key}': {some_dict[key]}")


##
points_dict = {"A": (1, 2),
               "B": (-2, 4),
               "C": (0, 6)}


test_value = " Я просто строка"


print_dict(points_dict, test_value)