
# 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. Напечатать столько раз my_symbol, сколько он встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# bla
# bla

# my_str = "blablablablacar"
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# if count > 0:
#     while count > 0:
#         count = count - 1
#         print(my_symbol)
# else:
#     print("Wrong!!!!")

my_str = str(input("Введите строку"))
my_symbol = str(input("Введите искомое в строке"))
count = my_str.count(my_symbol)
if count > 0:
    while count > 0:
        count = count - 1
        print(my_symbol)
else:
    print("Wrong!!!!")

#####################################################





#2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2
# ##

my_str = str(input("Введите строку"))
my_symbol = str(input("Введите искомое в строке"))
count = my_str.count(my_symbol)
print(f"Совпадений: {count}")

#####################################################

