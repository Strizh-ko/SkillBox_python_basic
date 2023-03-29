import re

numbers_lst = ['9999999999', '999999-999', '99999x9999', '8952589392']
for num, phone in enumerate(numbers_lst):
    if re.fullmatch(r'\b[89]\d{9}\b', phone):
        print(f'{num + 1}й номер: все ок')
    else:
        print(f'{num + 1}й номер: не подходит')