n = int(input("Введите количество пар слов: "))
syn_list = []
for i in range(n):
    word_list = {word for word in (input(f'{i + 1}я пара: ')).lower().split() if word.isalpha()}
    syn_list.append(word_list)

flag = False
while flag == False:
    word = input("\nВведите слово: ").lower()
    for syn in syn_list:
        if word in syn:
            word = {word}
            for syn in syn.difference(word):
                print('Синоним:', str(syn).title())
                flag = True
            break
    else:
        print("Такого слова в словаре нет.")
