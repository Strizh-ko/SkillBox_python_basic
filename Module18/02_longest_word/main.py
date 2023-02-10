line = input('Введите строку: ').split()

print("Самое длинное слово:", max(line, key=len))
print('Длина этого слова:', max([len(word) for word in line]))