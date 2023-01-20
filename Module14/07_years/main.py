a = int(input("Введите первый год: "))
b = int(input("Введите второй год: "))

print(f"Годы от {a} до {b} с тремя одинаковыми цифрами:")

def find_num(a, b):
    for i in range (a, b + 1):
    n = str(i)
    a = str(a)
    replace()