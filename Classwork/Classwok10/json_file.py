# import json  # модуль работы с форматом json
#
# my_dict = {"name": "John", "age": 30}
# #
# my_json = json.dumps(my_dict)  # преобразует словарь в строку. dumps - dump string
# print(my_json, type(my_json))
# print('---------------------------------')
# #
# # my_json = json.dumps(my_dict, indent=2)  # indent форматирует вид СТРОКИ!!!.
# # print(my_json)
# # print(type(my_json))
# #
# print('---------------------------------')
# my_dict_2 = json.loads(my_json)  # преобразует строку в словарь. loads - load string
# print(my_dict_2, type(my_dict_2))
#
# print('---------------------------------')
#
# outfile = "new.json"   # имя файла
# data = my_dict          # данные для записи в файл
#
# with open(outfile, 'w') as json_file:
#     json.dump(data, json_file)      # dump - dump object
# #
# with open(outfile, 'r') as json_file:
#     data = json.load(json_file)     # load - load object
# print(data, type(data))
