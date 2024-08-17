def check_rad(x, y, r):
    if ((x ** 2) + (y ** 2)) ** 0.5 <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки рядом нет")

print("Введите координаты монетки:")
x = float(input("X: "))
y = float(input("Y: "))
r = float(input("Введите радиус: "))

check_rad(x, y, r)

