n = int(input("Введите количество заказов: "))
data = dict()
for i in range(n):
    order = input(f"Заказ №{i+1}: ").split()
    if order[0] not in data:
        data[order[0]] = dict()
        data[order[0]][order[1]] = int(order[2])
    elif order[1] not in data[order[0]]:
        data[order[0]][order[1]] = int(order[2])
    else:
        data[order[0]][order[1]] += int(order[2])

for name in data:
    print(f'\n{name}:')
    for pizza in data[name]:
        print(f'        {pizza}: {data[name].get(pizza)}')