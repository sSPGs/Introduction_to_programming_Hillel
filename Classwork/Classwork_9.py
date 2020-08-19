'''1.Функции (Аргументы, аргументы по умолчанию, )
 2. Работа с файлами, менеджер контекстов
 3. Практическая работа
4. Рекурсия '''

####
'''1.Функции Аргументы, аргументы по умолчанию'''
'''(1) - аргументы передаются позиционно (tuple)
   (2) - аргументы могут передаваться с ключами (dict)
   (3) - в начале позиционные аргументы потом именованые'''
# def modify_string(my_string: str, symbol: str, number: int):
#     my_string = f'{symbol * number}{my_string}{symbol * number}'
#     return my_string
#
# def print_string(my_string: str, symbol: str, number: int):
#     my_string = f'{symbol * number}{my_string}{symbol * number}'
#     return my_string
#
#
#
# def create_lines_under_above_string(my_string, symbol= "*"):
#      add_str = symbol * len(my_string)
#      new_str = f"{add_str}\n{my_string}\n{add_str}"
#      print(new_str)
# modify_string_and_print("WTFFFFFFFFFFF",)
#
#
#
# def my_funcion(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# my_funcion(1, '123,', (1, 2,3), **{'zxc': 1, 'sdf':4}, qwe=1, asd=4)


'''                 2. Работа с файлами                     '''

# file = open('README.md', 'r')
# lines = file.read()
# print(lines)
# file.close()
# '''Читать'''
# with open('README.md', 'r') as file:
#     lines = file.read()
#     print(lines)
# print("hello")
#
# '''Писать'''
# with open('test.txt', 'w') as file:
#     file.write('Hello\n')
#     file.writelines(['asd, asdsa, sada, sadad'])
#     file.writelines(lines)

'''1-  создать папку tmp если её нет'''
import os

def create_folder(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
create_folder('tmp')

'''2-  создать строку алфавита без модуля string'''

alphabet = [chr(numb) for numb in range(ord('a'), ord('z') + 1)]
alphabet = ''.join(alphabet)
print(alphabet)

'''3-   в папку tmp положить файл alphabet.txt в которой записать этот алфавит'''

def save_file(filename, path, data: str):
    filename_with_pass = os.path.join(path, filename)
    with open(filename_with_pass, "w") as file:
        file.write(data)

save_file("alphabet.txt", 'tmp', alphabet)