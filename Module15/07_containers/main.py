n = int(input("Количество контейнеров: "))
list_cont = []

for i in range(1, n+1):
    mass = int(input(f"Введите массу {i} контейнера: "))
    list_cont.append(mass)

mass = int(input('\nВведите массу нового контейнера: '))

count = 0
for i in range(len(list_cont)):
    if mass <= list_cont[i]:
        count += 1
    else:
        break

print('\nНомер, который получит новый контейнер:', count+1)
