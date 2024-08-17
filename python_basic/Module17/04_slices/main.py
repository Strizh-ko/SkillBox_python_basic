alphabet = 'abcdefg'

text = alphabet[:]
print('Копия:', text)

text = alphabet[:: -1]
print('В обратном порядке:', text)

text = alphabet[:: 2]
print('Каждый второй элемент:', text)

text = alphabet[1:: 2]
print('Каждый второй элемент после первого:', text)

text = alphabet[:1]
print('До второго:', text)

text = alphabet[: len(alphabet)-2 : -1]
print('С конца до предпоследнего:', text)

text = alphabet[3:4]
print('С 3 по 4:', text)

text = alphabet[len(alphabet)-3::]
print('Последние три элемента:', text)

text = alphabet[3:5]
print('в диапазоне индексов от 3 до 4:', text)

text = alphabet[4:2:-1]
print('в диапазоне индексов от 3 до 4:', text)

