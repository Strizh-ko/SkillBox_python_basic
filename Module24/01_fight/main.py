import random

class Warriors:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def iscorpse(self):
        if self.hp == 0:
            print(f'\n{self.name} помер!')


def kick(agressor):
    if agressor == war1.name:
        war2.hp -= 20
    else:
        war1.hp -= 20
    return war1.hp, war2.hp


war1 = Warriors("Сэр Василий")
war2 = Warriors('Сэр Егор')

while (war1.hp and war2.hp) != 0:
    print(f'\n{war1.name} - {war1.hp}hp. {war2.name} - {war2.hp}hp.')
    agressor = random.choice((war1.name, war2.name))
    print(f"{agressor} наносит удар!")
    kick(agressor)
    war1.iscorpse()
    war2.iscorpse()