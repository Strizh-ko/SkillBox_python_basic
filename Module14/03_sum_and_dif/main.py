def count_symbol(n):
    count = 0
    for i in n:
        count += 1
    print ("Колво символов:", count)
    return count

def summ_simbol(n):
    summ = 0
    n = int(n)
    while n > 0:
        summ += n % 10
        n //= 10
    print("Сумма чисел:", summ)
    return summ

n = input("Введите целое положительное число: ")

count = count_symbol(n)
summ = summ_simbol(n)

print("Разность суммы и количества цифр: ", summ - count)


