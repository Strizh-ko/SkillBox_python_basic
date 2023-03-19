import functools


def callback(key: str):
    def intermediate_func(func):
        app[key] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # app[key] = func            # Не понимаю, почему эта строчка не выполняется, если ее прописать здесь вместо 6й строки
            rez = func(*args, **kwargs)
            return rez

        return wrapper
    return intermediate_func


app = {}

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')