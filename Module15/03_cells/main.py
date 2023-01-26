sheet = []
n = int(input("Введите количество клеток: "))

for rank in range(1, n + 1):
    eff = int(input(f"Эффективность {rank} клетки: "))
    if eff < rank:
        sheet.append(eff)

print("Неподходящие значения:", end = " ")
for i in range(len(sheet)):
    print(sheet[i], end = " ")