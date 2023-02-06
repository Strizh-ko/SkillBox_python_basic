def cypher(char, k):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if char in alphabet:
        if alphabet.index(char) + k > len(alphabet) - 1:
            n_char = alphabet[alphabet.index(char) + k - len(alphabet)]
        else:
            n_char = alphabet[alphabet.index(char) + k]
    else:
        n_char = char
    return n_char

word = input("Введите текст: ")
k = int(input("Введите сдвиг: "))
word_cypher = ""

for char in word:
    word_cypher += cypher(char, k)

print('Зашифрованное сообщение:', word_cypher)
