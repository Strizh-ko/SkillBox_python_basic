n = int(input("Введите количество человек: "))
tree = dict({'Peter_I': 0, 'Alexei': 1, 'Anna': 1, 'Elizabeth': 1, 'Peter_II': 2, 'Peter_III': 2, 'Paul_I': 3, 'Alexander_I': 4, 'Nicholaus_I': 4})
for i in range(1, n):
    pair = input(f"{i}я пара: ").split()
    if pair[1] not in list(tree.keys()):
        tree[pair[1]] = 0
        tree[pair[0]] = 1
    else:
        tree[pair[0]] = tree.get(pair[1]) + 1
    print(tree)

for name in sorted(tree):
    print(name, tree[name])