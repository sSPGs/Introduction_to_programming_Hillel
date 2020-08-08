# 1. Дано целое число (int). Определить сколько нулей в этом числе.

######################################################
#
# numb = 1021284010000000122310355653043015134
# numb = str(numb)
# print(numb.count("0"))
######################################################


#4. Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.
# Если my_list [1,2,3,4], то new_list [2,3,4,1]
####################################################



my_list = [1, 2, 3, 4]

new_list = my_list.copy()
# my_list = str(my_list)
index_list = len(my_list)

for index_list in new_list:
    index_list -= 1
    if index_list % 2 == 0:
        my_list = list(my_list)
        index_4et = index_list
        print(f'''Четные:{index_4et}''')

    elif index_list % 2 != 0:
        index_He4et = index_list
        print(f'''Нечетные:{index_He4et}''')

# print(index_a)

# print(f'''{new_list[0:-1:-1]}''')

    # new_list.append(index_list)


# new_list = new_list[2::-1]
# # new_list = my_list[::-1]
# len_my_list = len(my_list)
# my_list.index(len_my_list)
# # new_list = new_list[2::-1]
# new_list.append(my_list[-4])









####################################################

