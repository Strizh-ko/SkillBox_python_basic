sheet = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_sheet = []

for i_name in range(0, len(sheet), 2):
    new_sheet.append(sheet[i_name])

print("Первый день:", new_sheet)