

my_list = ["5 Horse", '123', '5135', '3624', "13_153", '135']

new_my_list = my_list.copy()
list_to_print = list()

for idx_n_list, val_n_list in enumerate(new_my_list):
    if not idx_n_list % 2:
        list_to_print.append(my_list[idx_n_list])
    else:
        list_to_print.append(my_list[idx_n_list][::-1])


print(f"TASK 1:::> {list_to_print}")


#######################################################################


my_list = ["12as12", "as12sa", "sa12sa", "a12a", "12hfdf", "122ssss"]

new_my_list = my_list.copy()
mod_list = []

for i_val in new_my_list:
    if i_val[0] == 'a':
        mod_list.append(i_val)

print(f"TASK 2:::> {mod_list}")
#######################################################################



my_list = ["12as12", "as12sa", "sa12sa", "a12a", "12hfdf", "122ssss"]

val_k = []

for key in my_list:
    cnt = int(len())
    for val in key[cnt - 1]:
        cnt += 1
        print(val)


print(val_k)









#######################################################################
my_list_int_and_str = [121, 'fjkjk', 3321, '300dsfgsd']
my_list_only_str = []

for key, val in enumerate(my_list_int_and_str):
    if type(val) == str:
        my_list_only_str.append(val)

print(f"TASK 4:::> {my_list_only_str}")

#######################################################################


my_str = 'qwevrtasdfqbwertasdf324'
set_mystr = set(my_str)
res = ''.join([i for i in set_mystr if my_str.count(i) == 1])
print(f"TASK 5:::> {res}")

#######################################################################

my_str_1 = "dfgvbhnjmkk,./852611as4548654a21448641864564seasd213231321151!!!56"
my_str_2 = "dfgvbhnjmkk,.asassd55454541231212312afdsanjhasd41864564se56646456!"
sum_my_str = my_str_1 + my_str_2
# print(set(sum_my_str))
print(f"TASK 6:::> {set(sum_my_str)}")

#######################################################################
my_str_7_1 = 'a1234sdfgh1234'
my_str_7_2 = 'asdfgh1234'

my_str_7_set = list()
my_str_7_set.extend(my_str_7_1 + my_str_7_2)

print(f"TASK 7:::> {set(my_str_7_set)}")



#######################################################################

person = {"Фамилия": "Гречуха",
          "Имя": "Владимир",
          "Возраст": 27,
          "Проживание": {
              "Страна": "Украина",
              "Город": "Днепр",
              "Улица": "Владимира Антоновича",
          },
          "Работа": {
              "Наличие": "Да",
              "Должность": "Инженер компьютерных систем"
          }
          }

print(f"TASK 8:::> {person}")

#######################################################################
dict_tort = {"Коржи": {
    "Мука": 12,
    "Молоко": 12,
    "Масло": 12312,
    "Яйцо": 121312,
},
    "Крем": {
        "Сахар": 12,
        "Масло": 12,
        "Ваниль": 12312,
        "Сметана": 121312,
    },
    "Глазурь": {
        "Какао": 12,
        "Сахар": 12,
        "Масло": 12312,
    }
}

print(f"TASK 9:::> {dict_tort}")

#######################################################################
