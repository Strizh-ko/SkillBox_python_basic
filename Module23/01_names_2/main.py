def cnt_sym_txt(filename):
    cnt_sym = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for i_line, line in enumerate(file):

            if '\n' in line:
                line = line[:len(line)-1]

            try:
                if len(line) < 3:
                    raise BaseException
            except BaseException:
                print(f'Если что, {i_line + 1}-я строка сильно коротка!')
            finally:
                cnt_sym += len(line)

    return cnt_sym

print('Общее количество символов:', cnt_sym_txt('people.txt'))