'''
'''
import json
import re

"""
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
"""


def read_json(filename_with_path):
    with open(filename_with_path, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def sort_dict_key_for_surname(value_dict:dict) -> str:
    return value_dict["name"].split(" ")[-1]

def get_sorted_by_surname(filename_with_path:str) -> list:
    sorted_by_surname = sorted(read_json(filename_with_path), key=sort_dict_key_for_surname)
    return sorted_by_surname

def sort_dict_key_for_death(value_str:dict) -> int:
    date = re.findall(r'[0-9]{1,4}', value_str["years"])
    if date:
        date = int(date[-1])
    else:
        date = 0
    date = (-1) * date if "BC." in value_str["years"] else date
    return date

def get_sorted_by_death(filename_with_path:str) -> list:
    sorted_by_death = sorted(read_json(filename_with_path), key=sort_dict_key_for_death)
    return sorted_by_death

def sort_dict_key_by_word_count(text:dict) -> int:
    return len(text["text"].split(" ")) # Разбил на слова

def get_sorted_by_word_count(filename_with_path:str) -> list:
    sorted_by_len_text = sorted(read_json(filename_with_path), key=sort_dict_key_by_word_count)
    return sorted_by_len_text