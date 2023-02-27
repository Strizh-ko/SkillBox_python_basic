def reg_sort(data_file):
    with open(data_file, 'r', encoding='utf-8') as registrations:
        for line in registrations:
            data_lst = line.split()

            with open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad:
                try:
                    if len(data_lst) != 3:
                        raise IndexError
                    if not data_lst[0].isalpha():
                        raise NameError
                    if "@" and '.' not in data_lst[1]:
                        raise SyntaxError
                    if int(data_lst[2]) <= 10 or int(data_lst[2]) >= 99 or not data_lst[2].isdigit():
                        raise ValueError

                except IndexError:
                        reg_bad.write(' '.join(data_lst) + '    -    НЕ присутствуют все три поля\n')
                except NameError:
                        reg_bad.write(' '.join(data_lst) + '    -    Поле «Имя» содержит НЕ только буквы\n')
                except SyntaxError:
                        reg_bad.write(' '.join(data_lst) + '    -    Поле «Имейл» НЕ содержит @ и . (точку)\n')
                except ValueError:
                        reg_bad.write(' '.join(data_lst) + '    -    Поле «Возраст» НЕ является числом от 10 до 99\n')

                else:
                    with open('registrations_good.log', 'a', encoding='utf-8') as reg_good:
                        reg_good.write(' '.join(data_lst) + '\n')

reg_sort('registrations.txt')