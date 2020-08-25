import os


"""1) функции передаем полный путь к файлу в виде строки в формате "./path/to/file/filename.ext",
где точка означает текущую директорию.
(Это универсальный способ задать путь. Пользователи виндовс можете почитать это:
https://stackoverflow.com/questions/2953834/windows-path-in-python)
Функция возвращает два параметра: название файла и путь к папке.
Пример использования:
filename, folder_path = first_function(path)"""

print("#########################################ONE##################################################################")

def path_to_path_and_name(path):
    folder_path = os.path.abspath(path)
    filename = os.path.basename(path)
    print(f'Filename is {filename}, Path to file {folder_path}')


path_to_path_and_name('C:/temp/doc123.txt')

print("##############################################################################################################")
"""2) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает список ФАЙЛОВ из этой папки. Т.к. listdir возвращает файлы и подпапки,
то такой функционал иногда нужен.
Напомню, что есть метод os.path.isfile(path) который возвращает True, если path указывает на файл.
И обратите внимание на "Щелчек Таноса" из классной работы. Мы там склеиваем путь с помощью os.path.join()
Пример использования:
files = second_function(path)
Значение по умолчанию - текущая папка. Т.е. second_function() вернет файлы из текущей папки."""
print("###############################################TWO############################################################")
# 2
def list_dir(path='C:/temp'):
    filename_with_path = []
    for file in os.listdir(path=path):
        if path in os.path.isfile(file) == 0:

            filename_with_path = print(os.path.join(file))

            return filename_with_path

list_dir()
print("##############################################################################################################")

"""3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
Пример использования:
path_dict = third_function(path)
Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки."""
print("###############################################THREE############################################################")

def list_dir_dict(path='C:/temp'):


    for file in list(set(os.listdir(path=path))):
        dict_list = {'files': os.path.join(file), 'folders': os.path.abspath(path)}
        print(dict_list)

list_dir_dict()
print("##################################################################################################################")

"""4) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция создает пустые папки в данной директории по следующему правилу:
- если в этой директории нет подпапок - создает папку 'tmp'
- если в этой директории есть подпапки - создает папки в названии которых дописываем '_tmp'.
Пример. Есть подпапка 'test'. значит создаем 'test_tmp'"""
print("###############################################FOUR############################################################")


