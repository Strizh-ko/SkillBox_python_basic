class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('\nКартошка прорастает!')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


class Gardener:
    name = 'Сэм'
    garden = []

    def weed(self, garden):
        garden.grow_all()

    def harvest(self, garden):
        for popato in garden:
            popato.state = 0
        print('\nУрожай собран')


garden = PotatoGarden(5)
Sam = Gardener()
Sam.garden = garden

for _ in range(3):
    Sam.weed(Sam.garden)

Sam.garden.are_all_ripe()
Sam.harvest(Sam.garden.potatoes)

Sam.garden.are_all_ripe()
