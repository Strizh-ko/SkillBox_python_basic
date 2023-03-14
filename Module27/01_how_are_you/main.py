from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:

    print('Привет! Ну что, как оно?')
    input()
    print('Понятно... Ладно, вот твоя функция:')
    return func



@how_are_you
def test() -> Any:
    print('<Тут что-то происходит...>')


test()