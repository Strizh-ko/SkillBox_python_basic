sheet = []
n = int(input("Количество элементов списка: "))
for i in range(1, n+1):
    num = int(input(f"Введите {i} число: "))
    sheet.append(num)
print("\nИзначальный список:", sheet)
k = int(input('Введите сдвиг: '))

new_sheeet = []
x = 0
for i in range(k, k + n):
    if i > len(sheet) - 1:
        new_sheeet.append(sheet[x])
        x += 1
    else:
        new_sheeet.append(sheet[i])

print(new_sheeet)