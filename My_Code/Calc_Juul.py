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
