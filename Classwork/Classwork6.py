# Возвести числа, стоящие на четных местах в квадрат и составить без изменений числа на нечетных местах
############################################
# my_list = [1, 2, 3, 5, 5, 6]

# for index, value in enumerate(my_list):
#     if index % 2:
#         print(value)
#     else:
#         print(value ** 2)

######Генератор Списков############
# my_list_str = ['343440', '16', '21663', '323', '4', '543', '623', '4443']
# print(my_list_str)

# my_list_int = [int(value) for value in my_list_str if int(value)]

# for val in my_list_str:
#     my_list_int.append(int(val))
#     if int(val) > 20:
#         print(val)

#Есть результат выполнения функции
# my_list_int = [int(val) for val in my_list_str]
# sqr_list = [val ** 2 for val in my_list_int]
# #Нет результат выполнения функции
# [print(qwe) for qwe in sqr_list]
# #Не имеет смысла
# result = [print(qwe) for qwe in sqr_list]
# print(result)
#
#
#
# print(my_list_int)

####################################3

####Множества (set)######

# str_1 = 'qwety not ytrewq'
# str_2 = 'srssdg'
#
# set_1 = set(str_1)
# set_2 = set(str_2)
#
# print(set_1.intersection(set_2)) # Поиск общих символов в стороках - Новый объект
# print(set_1.union(set_2)) # объединяет два множества в одно, только уникальное
# set_1.update(set_2)# добавление множества в другое множества
# new_set = set_1.union(set_2)
# print(new_set)
# my_set =set(str_)
# print(len(my_set)) # Вывод уникальных символов в строке
#
# for value in my_set:
#     print(value)
# for value in my_set:
#     print(value)
#
# print(list(str_))
# print((set(str_))) # поиск уникальных элементов

##############################################3#
####Множества (set)######
# my_list = [1, 2, 3, 4, 1, 3, 5, 5, 2]
#
# new_list = list(set(my_list)) # Перезапись списка - записует только уникальные значния
# print(new_list)
# ##############################################3#
#
# qwe = {1}
# print(type(qwe))

#######Задача: Вывести символ и его количество повторов#######################################3#


my_str = 'afggllhflyuasfyldfayfljv lavalafshlfscfcaflgsfcadshvas fgcahgecf.gdsfc jgsafc.j'

set_my_str = set(my_str) # SET

for symbol in set_my_str: # перебераем символы и выводим их количество по строчно
    print(f'{symbol}: {my_str.count(symbol)}')