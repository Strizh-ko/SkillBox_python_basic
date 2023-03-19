import functools
from datetime import datetime


def decdec(decorator):
    @functools.wraps(decorator)
    def wrapps(cls):
        names_cl_func = dir(cls)
        for name_func in names_cl_func:
            if not name_func.endswith('__'):
                cur_func = getattr(cls, name_func)
                dec_func = decorator(cur_func)
                setattr(cls, name_func, dec_func)
        return cls
    return wrapps


# def create_obj_time(cls):
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         print(f'Создается объект класса {cls.__name__}. {datetime.utcnow()}')
#         obj = cls(*args, **kwargs)
#         return obj
#     return wrapper


def log_methods(form_date: str):
    cur_form_date = ''
    for char in form_date:
        if char.isalpha():
            cur_form_date += '%'
        cur_form_date += char
    cur_time = datetime.strftime(datetime.today(), cur_form_date)

    def internal_func(func):
        @functools.wraps(func)
        def wrapps(*args, **kwargs):
            print(f"Запускается '{func.__name__}'. Дата и время запуска {cur_time}")
            rez = func(*args, **kwargs)
            print(f"Завершается '{func.__name__}'.")
            return rez
        return wrapps

    return internal_func



@decdec(log_methods("b d Y - H:M:S"))
class A:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@decdec(log_methods("b d Y - H:M:S"))
class B(A):

    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()