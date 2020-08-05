###########как можно красивее было сделать домашку#########################################
########################################
# my_str = str(input("Введите строку"))
# my_symbol = str(input("Введите искомое в строке"))
#
# count = my_str.count(my_symbol)
# result_str = f"{my_symbol}\n" * count
# print(result_str.strip())

# print(f"{my_symbol}\n" * count + "\n")
#############################################
#############################################
# my_str = "bla BLA car"
# my_str = my_str.lower()
#
# unique_symbol =  ''
#
# for symb in my_str:
#     if symb not in unique_symbol:
#         unique_symbol += symb
# print(len(unique_symbol), unique_symbol)
#############################################
#############################################



#
# 1.
# Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на четных местах в строке

# my_str = 'sadasfsagsgs'
# my_list = []
# my_str = list(my_str)
# a = my_str[::2] + my_list
#
# print(a)



# 2.
# Дана строка my_str, список str_index целых чисел в диапазоне от 0 до длинны строки, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с индексами из str_index
#


# str_index = [0, 2, 4, 5, 3, 5, 2, 2, 5, 3, 3]
# my_str = 'qwerty'
# my_list = []
#
# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)



#
# 3.
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и my_list_2 через один.

#Генератор RANGE  for value in range

my_list_1 = [10, 20, 30]
my_list_2 = [3, 4, 5]
my_result = []

if len(my_list_1) == len(my_list_2):
    for index in range(len(my_list_1)):
        my_result.append(my_list_1[index])
        my_result.append(my_list_2[index])

else:
    pass
print(my_result)

# 4.
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить четные элементы из my_list_1 и нечетные элементы из my_list_2.
#
# 5.
# Дано целое число. Определить сколько цифр в этом числе.
#
# 6.
# Дано целое число. Определить наибольшую цифру в этом числе.
#
# 7.
# Дано целое число. Составить число с цифрами в обратном порядке.
#
# 8.
# Дано целое число. Составить число с цифрами в порядке возрастания.
# """