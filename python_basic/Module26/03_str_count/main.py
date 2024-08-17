import os


my_path = os.path.abspath('..\\..\\Module26')


def str_count(my_path):
    cnt = 0
    for root, dirs, files in os.walk(my_path):
        for file in files:
            if file.endswith('.py'):
                with open(f'{os.path.join(root, file)}', 'r', encoding='utf-8') as cur_file:
                    for line in cur_file:
                        if line.startswith('#') or line.isspace():
                            pass
                        else:
                            cnt += 1
    return cnt


print('Общее количество не закоментированных не пустых строк:', str_count(my_path))

