#18

balon = float(15)
cart_ml = float(0.7)
result_balon = balon / cart_ml
cena_balon = 100

up_cart_four = 350
result_cart_four = up_cart_four / 4
total_cena_balon = cena_balon / result_balon
total_result = result_cart_four - total_cena_balon


print("______________________________Расчет выгоды от самозамеса в POD системе JUUL_______________________________")
print("##########################################################################################################")
print(f"****> Количество заправок c 15ml флакона солевой жидкости в картридж 0.7ml: {result_balon} раз")
print(f"****> Цена одной заправки c 15ml флакона солевой жидкости в картридж 0.7ml: {cena_balon / result_balon} UAH")
print("##########################################################################################################")
print(f"****> Цена одного готового картриджа с 0.7ml солевой жидкости: {result_cart_four} UAH")
print(f"****> Разница в цене между покупкой готовых картриджей и самостоятельной заправки {total_result} UAH \nПри большем количестве в {result_balon - 4} раз ")
print("######################$###################################################################################")
print("####################$#####################################################################################")

#1

# values = [1, 2, 3, 4, 5]
#
# print(f"Ответ 1: {type(values)}")
#####################################
#2

# values = (1, 2, 3, 4, 5)
#
# print(f"Ответ 2: {type(values)}")
#####################################
#3

# values = (1, 2, 3, 4, 5)
# values = list(values)
# print(f"Ответ 3: {type(values)}")

#####################################
#4

# values = [1, 2, 3, 4, 5]
# values = tuple(values)
# print(f"Ответ 4: {type(values)}")

#####################################
#5

# values = [1, 2, 3, 4, 5]
# result = []
#
# for value in values:
#     result.append(value)
#
# print(f"Ответ 5: {type(result)}{result}")
#
# #####################################
# #6
#
# values = [1, 2, 3, 4, 5]
# result = []
#
# for value in values[::-1]:
#     result.append(value)
#
# print(f"Ответ 6: {type(result)}{result}")
#
# #####################################
# #7
#
# values = [1, 2, 3, 4, 5]
#
# print(f"Ответ 7: Длинна списка {len(values)} элементов")
#
# #####################################
# #8
#
# values = [1, 2, 3, 4, 5]
#
# new_value = values + values[::-1]
#
# print(f"Ответ 8: {new_value}")
#
# #####################################
# #9
#
# values = [1, 2, 3, 4, 5]
# new_value = values
# new_value.append(6)
# print(f"Ответ 9: {values}")
#
# #####################################
# #10
#
# values = [1, 2, 3, 4, 5]
# new_value = values.copy()
# new_value.append(6)
# print(f"Ответ 10: {values}")
#
# #####################################
# #11
#
# values = [0] * 6
# values[0] = 1
# print(f"Ответ 11: {values}")
#
# #####################################
# #12
#
# value = 0
# values = [value] * 6
# value = 1
# print(f"Ответ 12: {values}")
#
# #####################################
# #13
#
# my_list = [0]
# values = [my_list] * 3
#
# print(f"Ответ 13: {values}")
#
# #####################################
# #14
#
# my_list = [0]
# values = [my_list] * 3
# my_list.append(1)
#
# print(f"Ответ 14: {values}")
#
# #####################################
# #15
#
# my_list = [0]
# values = [my_list.copy()] * 3
# my_list.append(1)
#
# print(f"Ответ 15: {values}")
#
# #####################################
# #16 - ответ: Бесконечное количество - хочешь проверить? Раскоментируй и запусти (потом верни назад комменты)
#
# # count = 10
# # a = "бесконеченый цикл = останови меня красным квадратиком"
# # while count > 0:
# #     print(f"Ответ 16: |Test| {a}")
#
# #####################################
# #17
#
# count = 10
# while count >= 0:
#     count -= 1
#     if count > 0:
#         print(f"Ответ 17: Вывод -> {count + 1} Test")
# #     count = []           # Можно закаментить
# #     count.append(count)       # Можно закаментить
#
# counts = 10
#
# while counts > 0:
#     counts -= 1
#
#     print(f"Вывод №: {counts} -> TEST")
#
#
#
#
# #####################################
# #17
#
# count = 10
# exit_flag = True
# while exit_flag:
#     count -= 1
#     if count > 0:
#         exit_flag = False
#         print(f"Вывело Test")