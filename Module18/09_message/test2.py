message = "Это задание очень! простое."

punct_list = ''
char_list = ''
for char in message:
    if char.isalpha():
        char_list += char
        punct_list += " "
    else:
        char_list += " "
        punct_list += char

punct_list = punct_list.split()
char_list = char_list.split()

print(punct_list)
print(char_list)