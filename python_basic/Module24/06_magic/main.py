class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    answer = 'Storm'


class Steam:
    answer = 'Steam'


class Mud:
    answer = 'Mud'


class Lightning:
    answer = 'Lightning'


class Dust:
    answer = 'Dust'


class Lava:
    answer = 'Lava'


a = Water()
b = Earth()
c = a + b
print(c.answer)