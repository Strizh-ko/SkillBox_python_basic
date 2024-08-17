import random


class KillError(Exception):
    def __init__(self):
        self.message = 'Буддист-программист сегодня мёртвый'


class DrunkError(Exception):
    def __init__(self):
        self.message = 'Буддист-программист напился. Праздник же...'


class CarCrashError(Exception):
    def __init__(self):
        self.message = 'Буддист-программист спровоцировал ДТП'


class GluttonyError(Exception):
    def __init__(self):
        self.message = 'В этот день буддист-программист нажрался фастфуда'


class DepressionError(Exception):
    def __init__(self):
        self.message = 'Буддист-программист весь день в печали'


def one_day():
    trespass = random.randint(1, 10)
    if trespass == 7:
        raise random.choice(err_lst)
    else:
        return random.randint(1, 7)


err_lst = (KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError())

day = 0
carma = 0
with open('karma.log', 'a', encoding='utf-8') as file:
    while carma < 500:
        day += 1
        try:
            carma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            file.write(f'День {day}: {error.message}\n')

