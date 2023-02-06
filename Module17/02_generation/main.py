def listgen(i):
    if i % 2 == 0:
        return 1
    else:
        return i % 5

n = int(input("Введите длину списка: "))
sheet = [listgen(x) for x in range(n)]
print("Результат:", sheet)