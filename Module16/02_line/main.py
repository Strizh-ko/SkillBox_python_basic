A_class = list(range(160, 177, 2))
B_class = list(range(162, 181, 3))

A_class.extend(B_class)
AB_class = []
for i in range(len(A_class)):
    AB_class.append(min(A_class))
    A_class.remove(min(A_class))

print('Отсортированный список учеников:', AB_class)