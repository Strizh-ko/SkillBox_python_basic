class Count:
    def __init__(self):
        self.cnt_call = 0


cnt = Count()


def counter(func):

    def wrapper_func(*args, **kwargs):
        cnt.cnt_call += 1
        func(*args, **kwargs)
        print(f'Функция {func.__name__} выполнена {cnt.cnt_call}-й раз')

    return wrapper_func


@counter
def test(x, y):
    """
    Функция делит x на y
    """
    c = x / y
    print('c =', c)


test(5, 1)
test(5, 2)

