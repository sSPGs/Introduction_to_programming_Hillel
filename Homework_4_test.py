#18



#1

values = [1, 2, 3, 4, 5]

print(f"Ответ 1: {type(values)}")
#####################################
#2

values = (1, 2, 3, 4, 5)

print(f"Ответ 2: {type(values)}")
#####################################
#3

values = (1, 2, 3, 4, 5)
values = list(values)
print(f"Ответ 3: {type(values)}")

#####################################
#4

values = [1, 2, 3, 4, 5]
values = tuple(values)
print(f"Ответ 4: {type(values)}")

#####################################
#5

values = [1, 2, 3, 4, 5]
result = []

for value in values:
    result.append(value)

print(f"Ответ 5: {type(result)}{result}")

#####################################
#6

values = [1, 2, 3, 4, 5]
result = []

for value in values[::-1]:
    result.append(value)

print(f"Ответ 6: {type(result)}{result}")

#####################################
#7

values = [1, 2, 3, 4, 5]

print(f"Ответ 7: Длинна списка {len(values)} элементов")

#####################################
#8

values = [1, 2, 3, 4, 5]

new_value = values + values[::-1]

print(f"Ответ 8: {new_value}")

#####################################
#9

values = [1, 2, 3, 4, 5]
new_value = values
new_value.append(6)
print(f"Ответ 9: {values}")

#####################################
#10

values = [1, 2, 3, 4, 5]
new_value = values.copy()
new_value.append(6)
print(f"Ответ 10: {values}")

#####################################
#11

values = [0] * 6
values[0] = 1
print(f"Ответ 11: {values}")

#####################################
#12

value = 0
values = [value] * 6
value = 1
print(f"Ответ 12: {values}")

#####################################
#13

my_list = [0]
values = [my_list] * 3

print(f"Ответ 13: {values}")

#####################################
#14

my_list = [0]
values = [my_list] * 3
my_list.append(1)

print(f"Ответ 14: {values}")

#####################################
#15

my_list = [0]
values = [my_list.copy()] * 3
my_list.append(1)

print(f"Ответ 15: {values}")

#####################################
#16 - ответ: Бесконечное количество - хочешь проверить? Раскоментируй и запусти (потом верни назад комменты)

# count = 10
# a = "бесконеченый цикл = останови меня красным квадратиком"
# while count > 0:
#     print(f"Ответ 16: |Test| {a}")

#####################################
#17

# count = 10
# while count >= 0:
#     count -= 1
#     if count > 0:
#         print(f"Ответ 17: Вывод -> {count + 1} Test")
#     count = []           # Можно закаментить
#     count.append(count)       # Можно закаментить

counts = 10

while counts > 0:
    counts -= 1

    print(f"Вывод №: {counts} -> TEST")




#####################################
#17

count = 10
exit_flag = True
while exit_flag:
    count -= 1
    if count > 0:
        exit_flag = False
        print(f"Вывело Test")