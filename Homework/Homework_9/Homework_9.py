import json
import csv
import random
import string

def create_random_string(len_string:int, symbols_for_string = (string.ascii_letters + string.digits + ",.;:" + " ")) -> str:
    my_string = ""
    while len(my_string) != len_string:
        my_string += symbols_for_string[random.randint(0, len(symbols_for_string) - 1)]
    return my_string

def create_random_insertion_positions(len_string:int, count_unique_positions = 9) -> list:
    insertion_positions = []
    while len(insertion_positions) != count_unique_positions:
        random_position = random.randint(1, len_string - 1)
        if random_position not in insertion_positions:
            insertion_positions.append(random_position)
    return insertion_positions

def past_symbol_in_random_string(len_string:int, symbol ="\n"):
    my_string = create_random_string(len_string)
    insertion_positions = create_random_insertion_positions(len_string)
    for position in insertion_positions:
        if my_string[position] == symbol:
            my_string = my_string.replace(my_string[position + 1], my_string[position + 1] + symbol, 1)
        elif my_string[position] != symbol:
            my_string = my_string.replace(my_string[position], my_string[position] + symbol, 1)
    return my_string

def create_data_for_txt_file(len_string=random.randint(100, 1000)) -> str:
    return past_symbol_in_random_string(len_string)

def create_random_key(len_key = 5) -> str:
    return create_random_string(len_key, string.ascii_lowercase)

def create_random_value() -> int:
    type_of_value = random.randint(1, 3)
    if type_of_value == 1:
        value = random.randint(-100, 100)
    elif type_of_value == 2:
        value = random.random()
    else:
        value = bool(random.randint(0, 1))
    return value

def create_random_data_for_json_file(key_count = random.randint(5, 20)) -> dict:
    data = {}
    while len(data) != key_count:
        data[create_random_key()] = create_random_value()
    return data

def create_random_m_list(random_len_data_m = random.randint(3, 10)) -> list:
    data_m = []
    while len(data_m) != random_len_data_m:
        data_m.append(random.randint(0, 1))
    return data_m

def create_random_data_for_csv_file(random_len_data_n = random.randint(3, 10)) -> list:
    data_n = []
    while len(data_n) != random_len_data_n:
        data_n.append(create_random_m_list())
    return data_n

def write_file_in_txt(filename_with_path:str):
    with open(filename_with_path, 'w') as txt_file:
        txt_file.write(create_data_for_txt_file())

def write_file_in_json(filename_with_path:str):
    with open(filename_with_path, 'w') as json_file:
        json.dump(create_random_data_for_json_file(), json_file)

def write_file_in_csv(filename_with_path:str):
    with open(filename_with_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(create_random_data_for_csv_file())

def file_writer(filename_with_path:str):
    if filename_with_path.endswith(".txt"):
        write_file_in_txt(filename_with_path)
    elif filename_with_path.endswith(".json"):
        write_file_in_json(filename_with_path)
    elif filename_with_path.endswith(".csv"):
        write_file_in_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")

file_writer("./testdir/1.txt")
file_writer("./testdir/1.json")
file_writer("./testdir/1.csv")
