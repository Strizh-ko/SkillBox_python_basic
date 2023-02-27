def check_line(line):
    data_lst = line.split()

    try:
        a, op, b, = int(data_lst[0]), data_lst[1], int(data_lst[2])
        if (len(op) != 1 and op != '//') or op not in '+-*//%':
            raise SyntaxError

    except ValueError:
        print('\nОпеанды не корректны.', end=' ')
        return fix(data_lst[0], data_lst[1], data_lst[2])

    except SyntaxError:
        print('\nОшибка оператора.', end=' ')
        return fix(data_lst[0], data_lst[1], data_lst[2])

    else:
        return a, op, b

def fix(a, op, b):
    answer = input(f'Строка: "{a} {op} {b}". Исправлять будем? (y/n): ')

    if answer == 'y':
        new_str = input('Введите строку корректно: ')
        return check_line(new_str)

    elif answer == 'n':
        return print('Как хотите...')

    else:
        print('Не понял...')
        return fix(a, op, b)

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return  a - b
    elif op == '*':
        return  a * b
    elif op == '/':
        return round(a / b, 2)
    elif op == '//':
        return  a // b
    elif op == '%':
        return a % b
    else:
        print('Ошибка оператора.', end=' ')
        return fix(a, op, b)

def text_calc(data_file):
    sumcnt = 0

    with open(data_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                a, op, b = check_line(line)
                sumcnt += calc(a, op, b)
            except TypeError:
                continue

    print('\nГотово! Сумма результатов:', sumcnt)

text_calc('calc.txt')
