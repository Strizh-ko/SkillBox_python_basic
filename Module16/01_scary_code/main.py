a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)

c5 = a.count(5)

for _ in range(c5):
    a.remove(5)

a.extend(c)

c3 = a.count(3)

print(c5, c3, a, sep='\n')
