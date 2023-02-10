f_name = input('Название файла: ')
for i in '@№$%^&\*()':
    if f_name.startswith(i):
        print('Ошибка: название начинается на один из специальных символов.')
        break
else:
    if f_name.endswith(".txt") or f_name.endswith(".docx"):
        print('Файл назван верно.')
    else:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
