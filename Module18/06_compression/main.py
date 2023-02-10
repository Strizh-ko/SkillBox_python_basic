line = input('Введите строку: ')

new_line = f"{line[1]}"
cnt = 1

for char in line[1:]:
    if new_line.endswith(char):
        cnt += 1
    else:
        new_line += f"{cnt}{char}"
        cnt = 1

print("Закодированная строка: ", new_line, cnt, sep='')
