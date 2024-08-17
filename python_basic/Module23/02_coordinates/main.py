import random


def f_p(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Ошибка в функции №1')
    else:
        return round(x / y, 2)


def f_m(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Ошибка в функции №2')
    else:
        return round(y / x, 2)


with \
        open("coordinates.txt", 'r', encoding='utf-8') as file, \
        open('result.txt', 'w', encoding='utf-8') as file_2:

    for line in file:
        nums_list = line.split()
        try:
            res1 = f_p(int(nums_list[0]), int(nums_list[1]))
            res2 = f_m(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError as error:
            print(error)
        else:
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            my_list = map(str, my_list)
            file_2.write('  '.join(my_list) + '\n')
