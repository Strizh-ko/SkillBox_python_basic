file = input('Название файла: ')
for i in '@№$%^&\*()':
    if file.startswith(i):
        print('Ошибка: название начинается на один из специальных символов.')
        break
else:
    if file.endswith(".txt") or file.endswith(".docx"):
        print('Файл назван верно.')
    else:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
