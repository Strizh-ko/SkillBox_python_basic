n = int(input("Количество элементов списка: "))
sheet = []
for i in range(1, n+1):
    num = int(input(f"Введите {i} число: "))
    sheet.append(num)
print("\nИзначальный список:", sheet)

while True:
    for i in range(len(sheet) - 1):
        if sheet[i] > sheet[i+1]:
            sheet[i], sheet[i + 1] = sheet[i+1], sheet[i]
            break
    else:
        break
print('Отсортированный список: ', sheet)