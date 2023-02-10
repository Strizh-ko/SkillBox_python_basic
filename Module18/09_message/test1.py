message = "Это задание очень! простое."

punct_list = ''
char_list = ''
for char in message:
    if char.isalpha():
        char_list += char
        punct_list += "0"
    else:
        char_list += "0"
        punct_list += char

punct_list = punct_list.split('0')
char_list = char_list.split('0')

print(punct_list)
print(char_list)

