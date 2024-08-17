n = int(input("Введите число: "))
def least_dev(n):
    k = int(n ** 0.5 + 1)
    for i in range(2, k):
        if n % i == 0:
            print("Наименьший делитель числа: ", i)
            break
    else:
        print("Число простое, наименьший делитель отличный от 1: ", n)

least_dev(n)