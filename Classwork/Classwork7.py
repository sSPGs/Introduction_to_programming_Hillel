# # №№№№№№№№№№Позиционное использование№№№№№№№№№№
# # 1) Ели значения не меняются
# points_tuple = ((1, 2), (-2, 4), (0, 6))
# print(points_tuple[1])
# # 2a) Ели меняются(Частично) порядок
# points_list = [(1, 2), (-2, 4), (0, 6)]
# # 2a) Ели меняются(полностью) порядок
# points_list_change = [[1, 2], [-2, 4], [0, 6]]
#
# # №№№№№№№№№№Использование по имени№№№№№№№№№№
# points_dict = {"A": (1, 2),
#                "B": (-2, 4),
#                "C": (0, 6)}
# print(points_dict["A"])
# #######ДОБАВИТЬ############
# point_d = (3, 5)
# points_dict["D"] = point_d
#
# points_dict.update({"D1": point_d})
# # d2 = {"D2": 0}
# # points_dict.update(d2)
#
#
# ##если есть ключ D2 то пропустить , а если нет то добавить в словарь по ключу D2
#
#
# test_point = (5, 7)
# print(points_dict)

# print(points_dict["D2"])

# BAD Practica

# try:
#     points_dict["D2"]:
#     print("qwe")
# except KeyError:
#     points_dict["D2"] = test_point

# GOOD Pracktica
#
#
# if points_dict.get("D2") is None:
#     points_dict["D2"] = test_point

#Можно проийти словарь FOR om

# for key in points_dict:
#     print(key, points_dict[key])
#
# print(list(points_dict.keys())) #Достать только ключи
# print(list(points_dict.values()))#Достать только значение





###  Модули в  Python ###
