#2) У вас есть список my_list с значениями типа int, и пустой список my_results. Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results. Задание выполнить с помощью цикла for.

#
my_list = [1, 21, 1244, 121, 41, 1221]

my_result = []

for index in my_list:
    if index > 100:
        my_result.append(index)
    else:
        pass
print(my_result)




#####################################################