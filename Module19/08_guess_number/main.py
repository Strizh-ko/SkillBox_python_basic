import random
x = int(input('Введите максимальное число: '))
n = random.randint(0, x)
possible_numbers = set(range(x + 1))

while True:
    numbers = input('\nНужное число есть среди вот этих чисел: ')
    if numbers == "Помогите!":
        print("Артём мог загадать следующие числа:", end=" ")
        for i in possible_numbers:
            print(i, end=' ')
        else: print()
    else:
        numbers = set([int(x) for x in numbers.split()])
        if {n} == numbers:
            print("Молодец угадал!")
            break
        elif n in numbers:
            possible_numbers &= numbers
            print('Ответ Артёма: Да')
        else:
            possible_numbers -= numbers
            print('Ответ Артёма: Нет')
