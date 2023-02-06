# def listgen(i):
#     if i % 2 == 0:
#         return 1
#     else:
#         return i % 5

n = int(input("Введите длину списка: "))
sheet = [1 if i % 2 == 0 else i % 5 for i in range(n)]
print("Результат:", sheet)