import random

def try777(out_file):
    num_sum = 0
    with open(out_file, 'w', encoding='utf-8') as file:
        while num_sum < 777:
            num = int(input('Введите число: '))
            num_sum += num

            if on_the_blade():
                file.write(str(num) + '\n')
            else:
                break
        else:
            print('Сегодня вам повезло!')

def on_the_blade():
    try:
        r_number = random.randint(0, 13)
        if r_number == 13:
            raise BaseException
    except BaseException:
        print('Не ваш день!')
        return False
    else:
        return True





try777("out_file.txt")




