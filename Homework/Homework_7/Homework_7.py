'''1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
Задание можно выполнить и через обычный цикл и через генератор списков'''
#####################################+######################################

print("-------------------------Задание 1-----------------------------------------------")
import random
random_list_print = []
cnt = 0
while cnt != 20:
    random_list = random.randrange(1, 100)
    random_list_print.append(random_list)
    cnt += 1
print(random_list_print)
print("-----------------Задание 1 выполнено---------------------------------------------")
print()
############################################################################
'''2) Создать словарь triangle в который записать точки A B C, и их координаты (кортежи) ,
созданные случайным образом с помощью модуля random.'''
############################################################################
print("-------------------------Задание 2--------------------------------")






print("-----------------Задание 2 НЕ выполнено--------------------------------")
print()
############################################################################
'''3) Создать функцию my_print, которая принимает строку и печатает ее
с тремя символами * вначале и в конце строки.
Пример:
my_str = 'I'm the string'
Печатает ***I'm the string*** '''
############################################################################
print("-------------------------Задание 3--------------------------------")
def my_print_1(val):
    print(f"***{val}***")
    return val
my_print_1(122)
print("----------------------Задание 3 выполнено------------------------")
print()
'''----------------------_____________________-------------------------'''


############################################################################
'''4)Создать функцию my_print, которая принимает строку и печатает ее
с символами * НАД и ПОД строкой. КОЛИЧЕСТВО СИМВОЛОВ * РАВНО КОЛИЧЕСТВУ СИМВОЛОВ В СТРОКЕ
Пример:
my_str = 'I'm the string'
Печатает
**************
I'm the string
**************  '''
############################################################################
print("-----------------Задание 4 -----------------------------------------")
def my_print_2(val):
    val = str(val)
    print(f"{len(val) * '*'}")
    print(f"{val}")
    print(f"{len(val) * '*'}")
    return val
my_print_2("fghjkl123124")
print("-----------------Задание 4 выполнено--------------------------------")
print()
'''----------------------_____________________-------------------------'''

############################################################################
''' 5) То же, что 4, но ответ должен выглядеть так:
********************
***I'm the string***
********************  '''
############################################################################
print("---------------------Задание 5 ------------------------------------")
def my_print_3(val):
    val = str(val)
    val = f"{'*' * 3}{val}{'*' * 3}"
    print(f"{len(val) * '*'}")
    print(f"{val}")
    print(f"{len(val) * '*'}")

    return val
my_print_3("fghjkl123124")
print("-----------------Задание 5 выполнено--------------------------------")
print()
###########################################################################