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

str_ = 'qwety not ytrewq'

print(list(str_))
print((set(str_))) # поиск уникальных элементов