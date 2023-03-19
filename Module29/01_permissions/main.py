import functools

user_permissions = ['admin']


def check_permission(user_rank: str):
    def intermediate_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user_rank in user_permissions:
                    rezult = func(*args, **kwargs)
                    return rezult
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: {func.__name__} не выполнено. Нехватает прав.')

        return wrapper
    return intermediate_func


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()