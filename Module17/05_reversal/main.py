text = input('Введите строку: ')
beg = text.index('h')
r_text = text[::-1]
end = len(text) - (r_text.index('h') + 1)
print(end , beg)
print('Развёрнутая последовательность между первым и последним h:', text[end - 1 : beg : -1 ])
