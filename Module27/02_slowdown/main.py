import time


def timeout(func):
    print('Подождем 2 секунды...')
    time.sleep(2)
    return func



@timeout
def test():
    print('<Тут что-то происходит...>')


test()