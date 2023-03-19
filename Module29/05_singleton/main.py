def singleton(cls):

    def wrapper(*args, **kwargs):
        if not wrapper.obj:
            wrapper.obj = cls(*args, **kwargs)
        return wrapper.obj

    wrapper.obj = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)