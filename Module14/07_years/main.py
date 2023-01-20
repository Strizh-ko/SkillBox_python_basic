def find_num(a, b):
    for i in range (a, b + 1):
        for n in range(10):
            i = str(i)
            n = str(n)
            selected_number = i.replace(n, "")
            if len(i) - len(selected_number) >= 3:
                print(i)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"Числа от {a} до {b} с тремя одинаковыми цифрами:")

find_num(a, b)