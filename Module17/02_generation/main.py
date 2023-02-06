

n = int(input("Введите длину списка: "))
sheet = [listgen(x) for x in range(n)]
print("Результат:", sheet)