def numb_line(a):
    if a > 0:
        numb_line(a - 1)
        print(a)


num = int(input('До какого числа вывадим числа? '))
numb_line(num)