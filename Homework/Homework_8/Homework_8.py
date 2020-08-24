import os
#1

def path_to_path_and_name(path):
    folder_path = os.path.abspath(path)
    filename = os.path.basename(path)
    print(f'Filename is {filename}, Path to file {folder_path}')


path_to_path_and_name('C:/temp/doc123.txt')

#2

def list_dir(path='C:/temp'):

    dir_list = print(os.listdir(path=path))

    return dir_list

list_dir()

"""3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
Пример использования:
path_dict = third_function(path)
Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки."""

