line_1 = input('Введите 1 строку: ')
line_2 = input('Введите 2 строку: ')

for i in range(len(line_2)):
    fp_line_2 = line_2[:len(line_2)-i]
    sp_line_2 = line_2[len(line_2)-i::]

    if sp_line_2 + fp_line_2 == line_1:
        print(f"Первая строка получается из второй со сдвигом {i}")
