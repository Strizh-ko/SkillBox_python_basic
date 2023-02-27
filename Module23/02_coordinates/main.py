import random

def f_p(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return round(x / y, 2)
    except ZeroDivisionError:
        print("Что-то пошло не так с первой функцией")

def f_m(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return round(y / x, 2)
    except ZeroDivisionError:
        print("Что-то пошло не так со второй функцией")



with open("coordinates.txt", 'r', encoding='utf-8') as file:
    with open('result.txt', 'w', encoding='utf-8') as file_2:

        for line in file:
            nums_list = line.split()
            res1 = f_p(int(nums_list[0]), int(nums_list[1]))
            res2 = f_m(int(nums_list[0]), int(nums_list[1]))

            number = random.randint(0, 100)
            try:
                my_list = sorted([res1, res2, number])
                my_list = map(str, my_list)
                file_2.write('  '.join(my_list) + '\n')
            except Exception:
                print("Что-то пошло не так при записи")


