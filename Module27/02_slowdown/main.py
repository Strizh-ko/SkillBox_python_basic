import time


def timeout(func):

    def wrapper(*args, **kwargs):
        print('Подождем 2 секунды...')
        time.sleep(2)
        result = func(*args, **kwargs)
        return result

    return wrapper



@timeout
def test():
    print('<Тут что-то происходит...>')


test()