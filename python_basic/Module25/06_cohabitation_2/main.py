class House:

    def __init__(self, food=50, money=100, c_food=30, dirt=0):
        self.food = food
        self.money = money
        self.c_food = c_food
        self.dirt = dirt
        self.all_rez = list()
        self.people = list()
        self.pets = list()
        self.rezult = {"Денег заработано": 0, 'Люди съели': 0, 'Кот съел': 0, 'Шуб в семье': 0}

    def all_calm(self):
        for person in house.people:
            person.happiness -= 10
            print('В доме срач, все люди грутсят.')


class Units:
    def __init__(self, name, house, saturation=30):
        self.name = name
        self.saturation = saturation
        self.house = house

    def __str__(self):
        return f'{person.name} - ссытость: {person.saturation}. Счастье: {person.happiness}'

    def eat(self):
        if house.food < 30:
            raise BaseException
        self.saturation += 30
        self.house.food -= 30
        print(f'{self.name} отъедается.')
        self.house.rezult['Люди съели'] += 30


class Human(Units):

    def __init__(self, name, people=True, happiness=100):
        super().__init__(name, house)
        self.happiness = happiness
        self.house.people.append(self)
        self.house.all_rez.append(self)

    def petting_cat(self):
        self.happiness += 5
        self.saturation -= 10
        print(f'{self.name} весь день гладит кота')


class Cat(Units):

    def __init__(self, name, house, saturation=30):
        super().__init__(name, house, saturation)
        house.pets.append(self)
        self.house.all_rez.append(self)

    def __str__(self):
        return f'{person.name} - ссытость: {person.saturation}.'

    def eat(self):
        if house.food < 10:
            raise BaseException
        self.saturation += 20
        self.house.c_food -= 10
        print(f'Кот {self.name}, конечно, ест.')
        self.house.rezult['Кот съел'] += 10

    def sleep(self):
        self.saturation -= 10
        print(f'Кот {self.name}, конечно, спит.')

    def get_mad(self):
        self.saturation -= 10
        house.dirt += 5
        print(f'Кот {self.name}, конечно, делает тыгыдык.')

    def do_plan(self):
        if self.saturation < 30:
            self.eat()
        else:
            self.sleep()


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def work(self):
        self.saturation -= 10
        self.house.money += 150
        print(f'{self.name} сегодня пошел на работу.')
        self.house.rezult['Денег заработано'] += 150

    def play(self):
        self.saturation -= 10
        self.happiness += 20
        print(f'{self.name} играет в танки.')

    def do_plan(self):
        if self.saturation < 30:
            self.eat()
        elif house.money < 600:
            self.work()
        elif self.happiness < 40:
            self.play()
        else:
            self.petting_cat()


class Wife(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def for_food(self):
        if house.money < 50:
            raise BaseException
        self.saturation -= 10
        self.house.food += 50
        self.house.money -= 50
        print(f'{self.name} идет в магазин за едой.')

    def for_cfood(self):
        if house.money < 30:
            raise BaseException
        self.saturation -= 10
        self.house.c_food += 30
        self.house.money -= 30
        print(f'{self.name} бежит в магазин за едой коту.')

    def mink(self):
        self.saturation -= 10
        self.happiness += 60
        self.house.money -= 350
        print(f'{self.name} купила себе очередную шубу.')
        self.house.rezult['Шуб в семье'] += 1

    def cleaning(self):
        self.saturation -= 10
        self.house.dirt -= 100
        print(f'{self.name} вычистила хату.')

    def do_plan(self):
        if self.saturation < 20:
            self.eat()
        elif house.food < 50:
            self.for_food()
        elif house.c_food < 60:
            self.for_cfood()
        elif house.dirt > 90:
            self.cleaning()
        elif house.money > 600:
            self.mink()
        else:
            self.petting_cat()


house = House()
husband = Husband('Дед Афанасий', house)
wife = Wife('Бабка', house)
cat = Cat("Ахмед", house)

for day in range(1, 366):
    print(f'\nДень {day}')
    if house.dirt > 90:
        house.all_calm()
    for person in house.all_rez:
        person.do_plan()
        print(person)

        if person.saturation < 0:
            print(f'{person.name} скончался с голодухи')
            raise BaseException
        if person in house.people:
            if person.happiness < 10:
                print(f'{person.name} задавила депрессия')
                raise BaseException

print("\nИтог")
print(house.rezult)
