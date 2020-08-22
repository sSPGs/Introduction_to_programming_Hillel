'''Форматы файлов json, csv'''

import json
import csv

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