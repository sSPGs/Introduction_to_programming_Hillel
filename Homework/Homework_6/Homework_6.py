
'''                            +
1. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
Задание сделать с использованием enumerate.'''
#######################################################################

# my_list = ["5 Horse", 123, 5135, 3624, "13 _ 153", 135]
#
# new_my_list = []
# new_my_list_Ne4et = []
# box_ne4 = []
#
#
# for ind, val in enumerate(my_list):
#     if ind % 2:
#         pass
#         if type(val) == int:
#
#             val = str(val)
#             new_my_list_Ne4et.append(val)
#             ne4 = new_my_list_Ne4et
#
#         else:
#             pass
#     else:
#         new_my_list.append(val)
#
# for ind_ne4, val_ne4 in enumerate(new_my_list_Ne4et):
#     val_ne4 = val_ne4[::-1]
#     box_ne4.append(val_ne4)
#     # print(f"ТИП VAL_NE4:::> {type(val_ne4)},{val_ne4}")
#     for i, val in enumerate(val_ne4):
#         val = list(val)
# a = new_my_list
# b = box_ne4
# new_my_list = a + b
# print(new_my_list)

#######################################################################
'''
2. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list у которых первый символ - буква "a".
'''
#######################################################################

my_list = ["baasasdasfaw", "askasknfmncxnb.a\e", "asfasfcxxczzzzz1`1112", "sasfadasf", "eet2344", "asdvxczzasfa", "asa","a1", "s1", "b1", "b2", "basd21", "as22211sv!", "a_a", "as1", "_a", "aaa2222"]


#######################################################################
'''
3. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list в которых есть символ - буква "a" на любом месте.
'''
#######################################################################

my_list = ["12as12", "as12sa", "sa12sa", "a12a", "12hfdf", "122ssss",]
a_list = []

for key, val in enumerate(my_list):
    if val in my_list.index([0]):
        if val in my_list:
            a_list.append(val)
        else:
            pass
print(a_list)





#######################################################################
'''
НЕМНОГО ТЕОРИИ ))
Мы можем сравнивать не только значение переменной, но и ее тип.
Например, чтобы проверить строка или нет:
if type(value) == str:
    print("Это строка")
else:
    print("Это не строка")
'''

'''
                         +
4. Дан список my_list в котором могум быть как строки так и целые числа.
Создать новый список в который поместить только строки из my_list.
'''
#######################################################################
# my_list_int_and_str = [121, 'fjkjk', 3321, '300dsfgsd']
# my_list_only_str = []
#
# for key, val in enumerate(my_list_int_and_str):
#     if type(val) == str:
#         my_list_only_str.append(val)
#
# print(my_list_only_str)

#######################################################################
'''                          +
5. Дана строка my_str. Вывести символы, которые встречаются в строке только один раз.
'''
#######################################################################

# my_str = 'qwevrtasdfqbwertasdf324'
# set_mystr = set(my_str)
# res = ''.join([i for i in set_mystr if my_str.count(i) == 1])
# print(res)

#######################################################################
'''                                  +
6. Даны две строки, вывести те символы, которые есть в обеих строках.
'''
#######################################################################

# my_str_1 = "dfgvbhnjmkk,./852611as4548654a21448641864564seasd213231321151!!!56"
# my_str_2 = "dfgvbhnjmkk,.asassd55454541231212312afdsanjhasd41864564se56!"
# sum_my_str = my_str_1 + my_str_2
# print(set(sum_my_str))


#######################################################################
'''
7. Даны две строки, вывести те символы, которые есть в обеих строках,
но в каждой только по одному разу.
'''
#######################################################################


#######################################################################
'''                                          +
8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
Фамилия
Имя
Возраст
Проживание
    Страна
    Город
    Улица
Работа
    Наличие
    Должность
'''
#######################################################################

# person = {"Фамилия": "Гречуха",
#           "Имя": "Владимир",
#           "Возраст": 27,
#           "Проживание": {
#               "Страна": "Украина",
#               "Город": "Днепр",
#               "Улица": "Владимира Антоновича",
#           },
#           "Работа": {
#               "Наличие": "Да",
#               "Должность": "Инженер компьютерных систем"
#           }
#           }
#
# print(person)

#######################################################################
'''                                          +
9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта, придумать и указать граммы для продуктов):
Составляющие
    Коржи
        Мука
        Молоко
        Масло
        Яйцо
    Крем
        Сахар
        Масло
        Ваниль
        Сметана
    Глазурь
        Какао
        Сахар
        Масло
'''
#######################################################################


# dict_tort = {"Коржи": {
#     "Мука": 12,
#     "Молоко": 12,
#     "Масло": 12312,
#     "Яйцо": 121312,
# },
#     "Крем": {
#         "Сахар": 12,
#         "Масло": 12,
#         "Ваниль": 12312,
#         "Сметана": 121312,
#     },
#     "Глазурь": {
#         "Какао": 12,
#         "Сахар": 12,
#         "Масло": 12312,
#     }
# }
#
# print(dict_tort)

#######################################################################
