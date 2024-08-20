word = input("Введите слово: ")
count = 0
temp = []
uniq = []
non_uniq = []


for sym in word:
    if sym in temp:
        non_uniq.append(sym)
    else:
        temp.append(sym)

for sym in temp:
    if sym not in non_uniq:
        uniq.append(sym)

print('Количество уникальных букв:', len(uniq))