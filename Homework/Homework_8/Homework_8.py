import os

"""1) функции передаем полный путь к файлу в виде строки в формате "./path/to/file/filename.ext",
где точка означает текущую директорию.
(Это универсальный способ задать путь. Пользователи виндовс можете почитать это:
https://stackoverflow.com/questions/2953834/windows-path-in-python)
Функция возвращает два параметра: название файла и путь к папке.
Пример использования:
filename, folder_path = first_function(path)"""

print("#########################################ONE##################################################################")


def path_to_path_and_name(path='C:/temp/doc123.txt'):
    folder_path = os.path.dirname(path)
    filename = os.path.join(folder_path, os.path.basename(path))
    return folder_path, filename


filename, folder_path = path_to_path_and_name()
print(f'ONE:::: >> [Filename is {filename}, Path to file {folder_path}]')


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
def list_dir(path='C:/temp/temp'):
    res = []
    for file in os.listdir(path):
        filename_path = os.path.join(path, file)
        if os.path.isfile(filename_path):
            res.append(filename_path)
    return res

res = list_dir()

print(f"TWO:::: >> {res}")
print("##############################################################################################################")

"""3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
Пример использования:
path_dict = third_function(path)
Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки."""
print(
    "###############################################THREE############################################################")
# 3

def list_dir_dict(path='C:/temp/temp'):
    folder = []
    files = []
    for file in list(os.listdir(path=path)):
        path_to_file = os.path.join(path, file)
        if os.path.isfile(path_to_file):
            files.append(file)
        else:
            folder.append(file)


    return files, folder

files, folder = list_dir_dict()
dct_dir = {'files': files, 'folders': folder}
print(f'THREE::::>>"{dct_dir}"')

print("##################################################################################################################")

"""4) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция создает пустые папки в данной директории по следующему правилу:
- если в этой директории нет подпапок - создает папку 'tmp'
- если в этой директории есть подпапки - создает папки в названии которых дописываем '_tmp'.
Пример. Есть подпапка 'test'. значит создаем 'test_tmp'"""
print("###############################################FOUR############################################################")
# 4

def make_dir(path='C:/temp/temp4'):

    if not os.path.isdir(path):
        os.path.isdir(path)
        os.mkdir(f'{path}/tmp')
    else:
        for i_mk in os.listdir(path):
            os.renames(os.path.join(path, i_mk), os.path.join(path,i_mk + '_tmp'))


        return i_mk


i_mk = make_dir()
print(i_mk)



