def sheet(n):
    a = []
    for i in range(n):
        x = int(input(f"{i + 1}-е число: "))
        a.append(x)
    return a

print("Введите числа первого списка:")
sheet1 = sheet(3)
print("Введите числа второго списка:")
sheet2 = sheet(7)

print("\nПервый список: ", sheet1)
print("Второй список: ", sheet2)

sheet1.extend(sheet2)
for num in sheet1:
    while sheet1.count(num) > 1:
        sheet1.remove(num)

print("\nНовый первый список с уникальными элементами:", sheet1)