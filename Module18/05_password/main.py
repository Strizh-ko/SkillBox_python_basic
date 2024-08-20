while True:
    password = input('Придумайте пароль:')
    digit = len([i for i in password if i.isdigit()])

    if digit < 3:
        print("Пароль должен содержать не менее 3х цифр")
    elif len(password) < 8:
        print("Пароль должен содержать не менее 8ми символов")
    elif password.islower():
        print('Пароль должен содержать хотя бы одну заглавную букву')
    else:
        print('Это надёжный пароль!')