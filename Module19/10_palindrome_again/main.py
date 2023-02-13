def frequency(text):
    freq = dict()
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

text = input("Введите текст: ")

freq = frequency(text)
count = 0
for i in freq:
    if freq[i] % 2 != 0:
        count += 1
    if count > 1:
        print('Нельзя сделать палиндромом')
        break
else:
    print('Можно сделать палиндромом')