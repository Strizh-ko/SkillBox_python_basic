n = int(input("Количество палок: "))
k = int(input('Количество бросков: '))

sticks = ["|" for i in range(n)]
for i in range(1, k + 1):
    print(f'Бросок {i}. Сбиты палки с номера', end=" ")
    L_i = int(input())
    print("по номер", end=" ")
    R_i = int(input())
    sticks[L_i - 1 : R_i] = ["." for _ in range(L_i, R_i + 1)]

print('Результат:', end=" ")
for i in sticks:
    print(i, end="")