import math


class MyMath:

    @classmethod
    def circle_len(cls, radius):
        len = 2 * math.pi * radius
        return len

    @classmethod
    def circle_sq(cls, radius):
        sq = math.pi * radius ** 2
        return sq

    @classmethod
    def cube_vol(cls, side):
        vol = side ** 2
        return vol

    @classmethod
    def sphere_surfase(cls, radius):
        surface = 4 * math.pi * radius ** 2
        return surface


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(side=2)
res_4 = MyMath.sphere_surfase(radius=2)

print(res_1)
print(res_2)
print(res_3)
print(res_2)