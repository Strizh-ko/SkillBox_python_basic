while True:
    ip = input('Введите IP: ').split('.')
    for part in ip:
        if part.isdigit() == False:
            print(f'{part} — это не целое число.')
            break
        elif int(part) < 0 or int(part) > 255:
            print(f'{part} — не в диапазоне от 0 до 255.')
            break
    else:
        if len(ip) != 4:
            print('Адрес — это четыре числа, разделённые точками.', len(ip))
        else: print(f'IP-адрес корректен.')
        break