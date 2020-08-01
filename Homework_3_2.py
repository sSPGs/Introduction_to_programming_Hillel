#У вас есть переменная value, тип - int.#
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = str(input("введите число"))
value = int(value)

new_value = value * 2 if value > 100 else value // 2

print(new_value)
#####################################################