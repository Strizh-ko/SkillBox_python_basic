class Property:
    def __init__(self, worth):
        self.worth = worth

    def all_tax(self):
        all_tax = apart.worth * apart.tax + car.worth * car.tax + house.worth * house.tax
        print('\nНалог на имущество: ', all_tax)
        if self.worth < all_tax:
            print('Роскошно живем! Денег на уплату налога не хватит!')
        else:
            print('Хорошо. Налог заплатить хватит.')


class Apartment(Property):
    tax = 0.001

    def __init__(self, worth):
        super().__init__(worth)


class Car(Property):
    tax = 0.005

    def __init__(self, worth):
        super().__init__(worth)


class CountryHouse(Property):
    tax = 0.002

    def __init__(self, worth):
        super().__init__(worth)


apart = Apartment(float(input('Сколько стоит ваша квартира? ')))
car = Car(float(input('А машина? ')))
house = CountryHouse(float(input('А дача то? Сколько стоит? ')))
money = Property(float(input('Ну а деньги то у нас сколько? ')))

money.all_tax()