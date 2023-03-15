from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        print('Привет! Ну что, как оно?')
        input()
        print('Понятно... Ладно, вот твоя функция:')
        result = func(*args, **kwargs)
        return result

    return wrapper


@how_are_you
def test() -> Any:
    print('<Тут что-то происходит...>')



test()