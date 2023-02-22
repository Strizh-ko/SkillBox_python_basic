num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))

def fibo(num_pos):
    if num_pos < 2:
        return 1
    return fibo(num_pos - 2) + fibo(num_pos - 1)

print('Число:', fibo(num_pos - 1))