#1

'''"1. Дано целое число (int). Определить сколько нулей в этом числе.'''
#####################################################

numb = 1021284010000000122310355653043015134

sum_numb = str(numb)
sum_total = sum_numb.count("0")

print(f'В числе {numb}\nКол-во НУЛЕЙ: {sum_total}')
print("######################################################")

####################################################

'''4.Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.
Если my_list [1,2,3,4], то new_list [2,3,4,1]'''

####################################################

my_list = [1, 2, 3, 4]
new_list = my_list[:]
del new_list[0]
new_list.append(my_list[0])
print(new_list)
print("######################################################")

####################################################

'''6. Дана строка в которой есть числа (разделяются пробелами). 
Например "43 больше чем 34, но меньше чем 56". Найти сумму ВСЕХ чисел в этой строке.'''

####################################################

my_str = "43 больше чем 34, но меньше чем 56"
my_str.split()
box_int = []

'''Цикл for iter_str_and_int in my_str:  '''
for iter_str_and_int in my_str:
    if iter_str_and_int in "1234567890":
        iter_str_and_int = int(iter_str_and_int)
        box_int.append((iter_str_and_int)) ## Выбераем из строки  цифры и помещаем в список box_int
    else:
        pass
print(sum(box_int))

print("######################################################")
####################################################



'''2. Дано целое число (int). Определить сколько нулей в конце этого числа.'''

####################################################












####################################################


'''3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить четные элементы 
из my_list_1 и потом нечетные элементы из my_list_2.'''


####################################################












####################################################


'''5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. 
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя!'''

####################################################










####################################################


'''6. Дана строка в которой есть числа (разделяются пробелами).
 Например "43 больше чем 34, но меньше чем 56".
 Найти сумму ВСЕХ чисел в этой строке. Для данного примера 133.'''

####################################################













####################################################


'''7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
 Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
  Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']'''
####################################################










####################################################


'''8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. В переменную sub_str поместить часть строки между этими символами. 
my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"'''
####################################################











####################################################

'''9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами. 
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".'''
####################################################













####################################################
'''10. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа), и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
 Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.'''
####################################################











####################################################