"""
1.
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на четных местах в строке
"""

my_str = "qwerty"
# решение через приведение типов
my_list = []
my_list += list(my_str[::2])
print(my_list)
# решение через цикл
my_list = []
for symbol in my_str[::2]:
    my_list.append(symbol)
print(my_list)


"""
2.
Дана строка my_str, список str_index целых чисел в диапазоне от 0 до длинны строки, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с индексами из str_index
"""
my_list = []
my_str = "qwerty"
str_index = [0, 5, 3, 3, 4]
for index in str_index:
    my_list.append(my_str[index])
print(my_list)

"""
3.
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и my_list_2 через один.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное
"""
my_list_1 = [10, 20, 30, 40]
my_list_2 = [3, 4, 5, 6, 7]
my_result = []
if len(my_list_1) == len(my_list_2):
    for index in range(len(my_list_1)):
        my_result.append(my_list_1[index])
        my_result.append(my_list_2[index])
else:
    if len(my_list_1) < len(my_list_2):  # проверяем, какой список короче.
        my_list_1, my_list_2 = my_list_2, my_list_1 # меняем списки местами. Длиннее дожен быть my_list_1
    for index in range(len(my_list_2)):
        my_result.append(my_list_1[index])
        my_result.append(my_list_2[index])
    print(my_result)
    print(my_list_1[len(my_list_2):])
    # my_result += my_list_1[len(my_list_2):]
    my_result.extend(my_list_1[len(my_list_2):]) # расширение одного списка элементами другого списка
print(my_result)
"""
4.
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить четные элементы из my_list_1 и нечетные элементы из my_list_2.
5.
Дано целое число. Определить сколько цифр в этом числе.
"""
number = 746527310
print(len(str(number)))
"""
6.
Дано целое число. Определить наибольшую цифру в этом числе.
"""
number = 746527310
number = str(number)
print(max(number))
"""
7.
Дано целое число. Составить число с цифрами в обратном порядке.
"""
number = 746527310
print(int(str(number)[::-1]))
"""
8.
Дано целое число. Составить число с цифрами в порядке возрастания.
"""
number = 746527310

# сортировка списка
my_list = [3, 5, -6]
my_list.sort()
print(my_list)

# сортировка копии списка
new_list = sorted(my_list)
print(my_list)
print(new_list)

# разбор ДЗ
my_str = "blablacar"
my_symbol = "bla"

count = my_str.count(my_symbol)
result_str = f"{my_symbol}\n" * count
print(result_str.strip())


my_str="bla BLA car"
my_str = my_str.lower()
unique_symbols = ''

for symb in my_str:
    if symb not in unique_symbols:
        unique_symbols += symb
print(len(unique_symbols), unique_symbols)