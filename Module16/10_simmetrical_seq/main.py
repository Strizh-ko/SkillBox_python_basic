n = int(input("Сколько чисел в последовательности? "))

seq = []
print('Введите числа: ')
for i in range(1, n + 1):
    seq.append(int(input(f"{i}-e: ")))
print('Последовательность:', seq)

newsyms = []
newsym_index = 0
while True:
    half = len(seq) // 2
    for i in range(half):
        bsym = seq[i]
        esym = seq[len(seq) - i - 1]
        if bsym != esym:
            seq.insert(len(seq) - newsym_index, seq[newsym_index])
            newsyms.insert(0, seq[newsym_index])
            newsym_index += 1
            break
    else:
        break

print('Нужно приписать чисел:', len(newsyms))
print('Сами числа:', newsyms)


