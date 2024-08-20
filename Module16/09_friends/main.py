n_fr = int(input("Количество друзей: "))
n_deb = int(input("Количество расписок: "))

balans = []
for _ in range(n_fr):
    balans.append(0)

debtors = []
creditors = []
debts = []
for i in range(n_deb):
    print(f"\n{i + 1}-я расписка:")
    debtors.append(int(input("Кому: ")))
    creditors.append(int(input("От кого: ")))
    debts.append(int(input("Сколько: ")))

for i in range(n_fr):
    while i + 1 in debtors:
        i_deb = debtors.index(i + 1)
        balans[i] -= debts[i_deb]
        balans[creditors[i_deb] - 1] += debts[i_deb]

        debtors.remove(i + 1)
        creditors.pop(i_deb)
        debts.pop(i_deb)

print('\nБаланс друзей:')
for i in range(n_fr):
    print(f'{i + 1}:', balans[i])