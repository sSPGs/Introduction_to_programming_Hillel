

#1


'''"1. Дано целое число (int). Определить сколько нулей в этом числе.'''
#####################################################

numb = 1021284010000000122310355653043015134

sum_numb = str(numb)
sum_total = sum_numb.count("0")

print(f'В числе {numb}\nКол-во НУЛЕЙ: {sum_total}')
print("######################################################")

####################################################

'''2. Дано целое число (int). Определить сколько нулей в конце этого числа.'''
####################################################

# numb_int = 10203000
# numb_str = str(numb_int)
#
# # numb_str = numb_str[::-1]
#
# len_numb_str = len(numb_str)
# idx_len_numb_str = len_numb_str - 1
# count_numb_str = 0
# print(numb_str)
#
# # while idx_len_numb_str >= 0:
# #     idx_len_numb_str -= idx_len_numb_str
#     if numb_str[idx_len_numb_str] == '0':
#         numb_str.count('0')
#         print(numb_str)
#     else:
#         break
#
# print(numb_str.count('0'))

####################################################

'''3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить четные элементы 
из my_list_1 и потом нечетные элементы из my_list_2.'''
####################################################

my_list_1 = [2, 6, 112, 12, 113, 1235]
my_list_2 = [5, 121, 5135, 3624, 13153, 135]
my_result = []

for idx, val in enumerate(my_list_1):
    if idx % 2:
        my_result.append(val)
    else:
        pass
for idx, val in enumerate(my_list_2):
    if idx % 2:
        pass
    else:
        my_result.append(val)
print(my_result)

#         ####################################################



'''4.Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.
Если my_list [1,2,3,4], то new_list [2,3,4,1]'''
####################################################

my_list = [1, 2, 3, 4]
new_list = my_list
new_list.append(new_list.pop(0))
print(new_list)
print("######################################################")

####################################################

'''5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. 
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя!'''

####################################################

my_list = [1, 2, 3, 4]
# my_list.insert(0, 2)
my_list.insert(0, my_list.pop(1))
my_list.insert(1, my_list.pop(2))
my_list.insert(2, my_list.pop(3))
print(my_list)




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

a, b = box_int[0], box_int[1]
a = str(a)
b = str(b)
ab = a+b
ab = int(ab)

c, d = box_int[2], box_int[3]
c = str(c)
d = str(d)
cd = c+d
cd = int(cd)

e, f = box_int[4], box_int[5]
e = str(e)
f = str(f)
ef = e + f
ef = int(ef)

res = (ab + cd + ef)
print(res)

print("######################################################")
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

my_str = "My_long str"

sub_str = my_str[5:9]
print(sub_str)



####################################################



'''9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами. 
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".'''
####################################################








####################################################

'''10. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
 Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.'''
####################################################














####################################################