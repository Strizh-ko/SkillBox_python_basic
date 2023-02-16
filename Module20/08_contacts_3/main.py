def choice():
    print("""1. Добавить контакт
2. Найти человека
Введите номер действия:""", end=" ")
    c = input()
    if c == "1":
        cont_import()
    elif c == "2":
        cont_find()
    else:
        print('Не корректное действие')

def cont_import():
    contact = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').lower().title().split())
    if contact in telbook:
        print('Такой человек уже есть в контактах.')
    else:
        tel = int(input('Введите номер телефона: '))
        telbook[contact] = tel
        print('Контакт успешно добавлен.')

def cont_find():
    surname = input('Введите фамилию для поиска: ').lower().title()
    for people, tel in telbook.items():
        if surname == people[1]:
            print(' '.join(people), tel)


telbook = {}
while True:
    choice()
    print('\nТекущий словарь контактов:', telbook)