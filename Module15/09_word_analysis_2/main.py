word = list(input('Введите слово: '))

new_word = []
l = len(word)
for char in range(-1,  - (l + 1), -1):
    new_word.append(word[char])

if word == new_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
