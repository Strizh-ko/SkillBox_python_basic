def decorator_with_args_for_any_decorator(decorator):
    def wrapper(*args, **kwargs):
        print(f'Переданные args и kwargs в декоратор "{decorator.__name__}":', args, kwargs)
        return decorator(*args, **kwargs)
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs):

    def arg_dec(func):
        def wrapper(*args, **kwargs):
            rez = func(*args, **kwargs)
            return rez
        return wrapper
    return arg_dec


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
