'''Форматы файлов json, csv'''

import json
import csv
def reader_txt(filename_with_path):
    data = ''
    with open(filename_with_path, "r") as txt_file:
        data = txt_file.read()
    return data

def reader_json(filename_with_path):
    pass

def reader_csv(filename_with_path):
    pass

def file_reader(filename_with_path):
    ext = filename_with_path.rsplit(".", 1)[-1]
    if ext == "txt":
        pass
    elif ext == "json":
        pass
    elif ext == "csv":
        pass
    else:
        raise Exception ("WTF!!! НЕВЕРНЫЙ ФОРМААААААТ!!!!!!!!")

file_reader("test.csv")