N = int(input("Количество человек: "))
K = int(input("Какое число в считалке? "))
print(f"Выбывает каждый {K}-й")
people = list(range(1, N + 1))

begin = 1
while len(people) > 1:
    print("\nТекущий круг людей:", people)
    print("Начало счета с номера:", begin)

    n = K // len(people)
    temp = people + (n+ 1) * people
    i_goodbye = temp.index(begin) + K - 1
    goodbye = temp[i_goodbye]
    people.remove(goodbye)

    print("Выбывает человек под номером", goodbye)
    begin = temp[i_goodbye + 1]

print('\nОстался человек под номером', people[0])