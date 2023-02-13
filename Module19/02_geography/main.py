how_many = int(input("Количество стран: "))
country = dict()
for i in range(how_many):
    line = (input(f'{i+1}я страна: ')).split()
    country[line[0]] = [city for city in line[1:]]

for i in range(1, 4):
    city = input(f"{i}й город: ")
    for i in country:
        if city in country[i]:
            print(f'Город {city} расположен в стране {i}')
        else:
            print(f'По городу {city} данных нет')