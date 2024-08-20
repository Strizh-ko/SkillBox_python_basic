message = "Хотя ,. возм:ожно и нет."

new_message = ''
char_list = ''
for char in message:
    if char.isalpha():
        char_list += char
    else:
        new_message += char_list[::-1] + char
        char_list = ''

print(new_message)

