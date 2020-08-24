import os
#1

def path_to_path_and_name(path):
    path = os.path.abspath(path)
    name = os.path.basename(path)
    print(f'Filename is {name}, Path to file {path}')
    return name and path

path_to_path_and_name('C:/temp/doc123.txt')

#2