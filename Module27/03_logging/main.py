import datetime, functools


def logging(func):
    print(f'Функция: ', func.__name__)
    print(func.__doc__)
    print()

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except (Exception) as error:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                cur_time = datetime.datetime.now()
                file.write(f'\n{str(cur_time)}: {error}')

        return func

    return wrapper_func



@logging
def test(x, y):
    """
    Функция делит x на y
    """
    c = x / y
    print('c =', c)

test(5, 0)
