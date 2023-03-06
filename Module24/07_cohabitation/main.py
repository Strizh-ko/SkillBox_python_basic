import random


class House:
    food = 50
    money = 0

    def __init__(self, name, saturation=50):
        self.name = name
        self.saturation = saturation

    def eat(self):
        self.saturation += 1
        House.food -= 1
        print(f'{self.name} покушал.')


    def work(self):
        self.saturation -= 1
        House.money += 1
        print(f'{self.name} работает.')

    def play(self):
        self.saturation -= 1
        print(f'{self.name} играет в бирюльки.')

    def magazine(self):
        House.food += 1
        House.money -= 1
        print(f'{self.name} идет в магазин за едой.')


person1 = House('Саня')
person2 = House('Адда')
person3 = House("Бабуля")
peole = [person1, person2, person3]


for day in range(1, 366):
    print(f'\nДень {day}')
    for person in peole:
        digit = random.randint(1, 6)
        if person.saturation < 20:
            person.eat()
        elif House.food < 10:
            person.magazine()
        elif House.money < 50:
            person.work()
        elif digit == 1:
            person.work()
        elif digit == 2:
            person.eat()
        else:
            person.play()

        print(f'{person.name} - ссытость: {person.saturation}. Число дня: {digit}')
        if person.saturation == 0:
            peole.remove(person)
            print(f'{person.name} скончался с голодухи')

    print(f'Конец дня. Ресурсы дома - Еда: {House.food}. Денег: {House.money}')
