import random


class House:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
        self.residents = list()


class Human:

    def __init__(self, name, house, saturation=50):
        self.name = name
        self.house = house
        self.saturation = saturation
        if self.house:
            self.house.residents.append(self)

    def eat(self):
        self.saturation += 1
        self.house.food -= 1
        print(f'{self.name} покушал.')

    def work(self):
        self.saturation -= 1
        self.house.money += 1
        print(f'{self.name} работает.')

    def play(self):
        self.saturation -= 1
        print(f'{self.name} играет в бирюльки.')

    def magazine(self):
        self.house.food += 1
        self.house.money -= 1
        print(f'{self.name} идет в магазин за едой.')


house = House()
person1 = Human('Саня', house)
person2 = Human('Адда', house)
person3 = Human("Бабуля", house)


for day in range(1, 366):
    print(f'\nДень {day}')
    for person in house.residents:
        digit = random.randint(1, 6)
        if person.saturation < 20:
            person.eat()
        elif house.food < 10:
            person.magazine()
        elif house.money < 50:
            person.work()
        elif digit == 1:
            person.work()
        elif digit == 2:
            person.eat()
        else:
            person.play()

        print(f'{person.name} - ссытость: {person.saturation}. Число дня: {digit}')
        if person.saturation == 0:
            house.residents.remove(person)
            print(f'{person.name} скончался с голодухи')

    print(f'Конец дня. Ресурсы дома - Еда: {house.food}. Денег: {house.money}')
