def frequency(text):
    freq = dict()
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def inv_frequency(freq):
    inv_freq = dict()
    for i in freq.keys():
        if freq[i] not in inv_freq:
            inv_freq[freq[i]] = []
        inv_freq[freq[i]].append(i)
    return inv_freq

text = input("Введите текст: ")
freq = frequency(text)

print('\nОригинальный словарь частот')
for i in sorted(freq):
    print(f'{i}:{freq[i]}', end=' ')

inv_freq = inv_frequency(freq)

print('\nИнвертированный словарь частот:')
for i in sorted(inv_freq):
    print(f'{i}:{inv_freq[i]}')

