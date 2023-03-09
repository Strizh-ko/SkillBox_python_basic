import math


class Car:

    def __init__(self, x=0, y=0, alpha=0):
        self.x = x
        self.y = y
        self.alpha = alpha

    def move(self):
        print('Выберите направление движения и расстояние.')
        corr_alpha = int(input("Угол отклонения от прежнего курса: "))
        s = int(input('Расстояние: '))
        self.move_calc(corr_alpha, s)

    def move_calc(self, corr_alpha=0, s=0 ):
        self.alpha += corr_alpha
        self.x += round(s * math.sin(round(math.radians(self.alpha), 2)))
        self.y += round(s * math.cos(round(math.radians(self.alpha), 2)))

    def info(self):
        print(f'Текущая позиция Автомобиля: X:{self.x}, Y:{self.y}, направление:{self.alpha % 360}')


class Bus(Car):

    def __init__(self, income=0, passengers=0):
        super().__init__()
        self.income = income
        self.passengers = passengers

    def move(self, corr_alpha=0, s=0):
        num = int(input("Введите изменение количества пассажиров? ('+/-'число) "))
        self.passangers_in_out(num)

        print('Выберите направление движения и расстояние.')
        corr_alpha = int(input("Угол отклонения от прежнего курса: "))
        s = int(input('Расстояние: '))
        self.pay(s)
        self.move_calc(corr_alpha, s)

    def passangers_in_out(self, num):
        self.passengers += num

    def pay(self, s):
        self.income += s * self.passengers * 10   # 10 - цена проезда за единицу расстояния

    def info(self):
        print(f'Текущая позиция Автобуса: X:{self.x}, Y:{self.y}, направление:{self.alpha % 360}.'
              f' Пассажиров в салоне: {self.passengers}. Заработок за сегодня: {self.income}')


car = Car()
bus = Bus()

while True:
    who = int(input('\nКто едет? (1 - Автомобиль, 2 - Автобус) '))
    if who == 1:
        car.move()
        car.info()
    elif who == 2:
        bus.move()
        bus.info()
    else:
        print('Неверно введен код ТС!')