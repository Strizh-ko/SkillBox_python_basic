site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(dct, key, **kwargs):

    if kwargs.get('deep') == None:
        deep = None
    elif int(kwargs.get('deep')) == 0:
        rez = None
        return rez
    else:
        deep = int(kwargs.get('deep')) - 1

    if key in dct:
        return dct[key]

    for next_dct in dct.values():
        if isinstance(next_dct, dict):
            rez = find_key(next_dct, key, deep=deep)
            if rez:
                break

    else:
        rez = None

    return rez


key = input("Введите искомый ключ: ")
ask = input('Хотите ввести максимальную глубину поиска? Y/N: ')
if ask.lower() == 'y':
    deep = int(input('Введите максимальную глубину: '))
else:
    deep = None

rez = find_key(site, key, deep=deep)
if rez:
    print('Ключ найден. Значение:', rez)
else:
    print('Такого ключа нет')



