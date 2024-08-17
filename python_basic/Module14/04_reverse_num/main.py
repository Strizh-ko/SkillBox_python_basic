def reverse_float(n):
    def reverse_int(i):
        result = ""
        while i > 0:
            result += str(i % 10)
            i //= 10
        return result

    n = str(n)
    int_part = ""
    frac_part = ""
    count = 0
    for i in list(n):
        if i == ".":
            count += 1
            continue
        if count == 0:
            int_part += i
        else:
            frac_part += i

    int_part = int(int_part)
    frac_part = int(frac_part)

    int_part = reverse_int(int_part)
    frac_part = reverse_int(frac_part)
    return float(int_part + "." + frac_part)


n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))

rev_n = reverse_float(n)
rev_k = reverse_float(k)

print ("\nПервое число наоборот:", rev_n)
print ("Второе число наоборот:", rev_k)

print ("Сумма:", rev_n + rev_k)
