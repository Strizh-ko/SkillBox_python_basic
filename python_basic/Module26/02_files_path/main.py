import os


my_path = os.path.abspath(os.path.sep)
direct = input('Введите имя искомого каталога: ')


def gen_files_path(direct:str, my_path):
    for root, dirs, files in os.walk(my_path):
        if direct in dirs:
            break
        else:
            for file in files:
                print(os.path.join(root, file))


gen_files_path(direct, my_path)

