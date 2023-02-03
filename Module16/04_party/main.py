guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

action = ''
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    action = input("Гость пришёл или ушёл? ")
    if action == "Пора спать" or action == "пора спать":
        break
    else:
        name = input("Имя гостя: ")
        if action == "пришёл" or action == "пришел":
            if len(guests) < 6:
                guests.append(name)
                print("Привет", name)
            else:
                print(f"Прости, {name}, но мест нет.")
        elif action == "ушел" or action == 'ушел':
            guests.remove(name)

print('Вечеринка закончилась, все легли спать.')