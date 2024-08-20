import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        circle_lst = []
        self.x = x
        self.y = y
        self.r = r

    def info(self):
        return self.x, self.y, self.r

    def square(self):
        s = math.pi * self.r ** 2
        return s

    def lenth(self):
        l = 2 * math.pi * self.r
        return l

    def increase(self, k):
        self.r = math.sqrt((self.square() * k)/math.pi)

    def intersection(self, tpl):
        gip = math.sqrt((self.x - tpl[0]) ** 2 + (self.y - tpl[1]) ** 2)
        if gip <= self.r + tpl[2]:
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')

cir1 = Circle(4, 3, 3)
cir2 = Circle(2, -2, 2)

cir1.intersection(cir2.info())