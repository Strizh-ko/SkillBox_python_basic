text = input("Введите текст: ")
text_vowel = [vchar for vchar in text if vchar in "ауоыиэяюёеАУОЫИЭЯЮЁЕ"]
print("Список гласных букв: ", text_vowel)
print('Длина списка: ', len(text_vowel))