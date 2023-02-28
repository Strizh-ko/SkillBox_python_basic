def line_check(data_lst):
    if len(data_lst) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    elif not data_lst[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif "@" and '.' not in data_lst[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    elif int(data_lst[2]) <= 10 or int(data_lst[2]) >= 99 or not data_lst[2].isdigit():
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    return


def reg_sort(data_file):
    with open(data_file, 'r', encoding='utf-8') as registrations,\
        open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad,\
        open('registrations_good.log', 'a', encoding='utf-8') as reg_good:

        for line in registrations:
            data_lst = line.split()
            try:
                line_check(data_lst)
            except (IndexError, NameError, SyntaxError, ValueError) as error:
                reg_bad.write(' '.join(data_lst) + f'    -    {error}\n' )
            else:
                reg_good.write(' '.join(data_lst) + '\n')

reg_sort('registrations.txt')