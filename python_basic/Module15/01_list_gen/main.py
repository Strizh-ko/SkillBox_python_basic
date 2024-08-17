sheet = []
n = int(input("Введите целое число N: "))

for i in range(1, n+1, 2):
    sheet.append(i)

print("Список из нечётных чисел от одного до N:", sheet)