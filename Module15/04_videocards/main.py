sheet = []
n_sheet = []
top = 0

n = int(input("Введите количество видеокарт: "))

for _ in range(n):
    mod = int(input("Видеокарта: "))
    sheet.append(mod)
    if mod > top:
        top = mod

print("Старый список видеокарт:", sheet)

for i in sheet:
    if i != top:
        n_sheet.append(i)

print('\nНовый список видеокарт:', n_sheet)