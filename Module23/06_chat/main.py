def chat(username):
    act = input(
"""\n1. Просмотр сообщений чата
2. Отправить сообщение.
Выберите действие: """
    )

    if act == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                print('\n       -=ЧАТ=-')
                print(''.join(chat.readlines()))
        except FileNotFoundError:
            print('\n   -=В чате пока пусто=-')
    elif act == '2':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as chat:
            chat.write(f'{username}: {message}\n')
    else:
        print('Непонятное действие. Требуется 1 или 2.')


username = input('Введите имя: ')
while True:
    chat(username)