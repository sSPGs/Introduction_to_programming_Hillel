#1
######################################################
numb = 1021284010000000122310355653043015134
print(f"1. Дано целое число {numb}. Определить сколько нулей в этом числе.")
numb = str(numb)
print(f'В числе {numb}\nКол-во НУЛЕЙ: {numb.count("0")}')
print("######################################################")
######################################################
#4
####################################################
print("4.Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.\nЕсли my_list [1,2,3,4], то new_list [2,3,4,1]")
my_list = [1, 2, 3, 4]
new_list = my_list[:]
del new_list[0]
new_list.append(my_list[0])
print(new_list)
print("######################################################")
####################################################
#6
####################################################
'''6. Дана строка в которой есть числа (разделяются пробелами). 
Например "43 больше чем 34, но меньше чем 56". Найти сумму ВСЕХ чисел в этой строке.'''

my_str = "43 больше чем 34, но меньше чем 56"
my_str.split()
box_str = []
box_int = []
box_int_sum = []
box_forward_string_to_int_step = ''

for iter_str_and_int in my_str:
    if iter_str_and_int in "1234567890":
        box_int.append((iter_str_and_int))
    else:
        box_str.append(iter_str_and_int)

box_forward_string_to_int_step = box_forward_string_to_int_step.join(box_int)
# print(f"BOX_STR {box_str}")
print(f"BOX_INT {(box_int)}")
print(f"box_forward_string_to_int_step::::::::::>>> {(box_forward_string_to_int_step)}")

box_forward_string_to_int_step = int(box_forward_string_to_int_step)

for itt_box_forward_int in box_int_sum:
    box_int_sum = box_int_sum.append(itt_box_forward_int)
    # print(box_int_sum)
print(f"ТИП box_forward_string_to_int_step {type(box_forward_string_to_int_step)}")
print(box_forward_string_to_int_step)

print(type(box_int_sum))

print(box_int_sum)
print("######################################################")

