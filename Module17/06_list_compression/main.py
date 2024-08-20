import random

sheet = [random.randint(0, 2) for _ in range(int(input("Количество чисел в списке: ")))]
print("Список до сжатия:", sheet)
for _ in range(sheet.count(0)):
    sheet.remove(0)
    sheet.append(0)

print("Список после сжатия:", sheet)