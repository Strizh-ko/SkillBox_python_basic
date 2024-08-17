def sheet(n):
    a = []
    for i in range(n):
        x = int(input(f"{i + 1}: "))
        a.append(x)
    return a

n_skates = int(input("Количество пар коньков: "))
print("Введите размеры каждой пары: ")
skates = sheet(n_skates)
n_people = int(input("\nКоличество человек: "))
print("Введите размеры ног каждого человека:")
people = sheet(n_people)

count = 0
while len(skates) > 0 and len(people) > 0:
    if min(people) > min(skates):
        skates.remove(min(skates))
    else:
        people.remove(min(people))
        skates.remove(min(skates))
        count += 1

print("Наибольшее кол-во людей, которые могут взять ролики:", count)