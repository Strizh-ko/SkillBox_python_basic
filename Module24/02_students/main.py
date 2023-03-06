import random


class Student:
    def __init__(self, name, group, gradelst):
        self.name = name
        self.group = group
        self.gradelst = gradelst

    def st_info(self):
        return self.name, self.group, sum(self.gradelst)/5


st1 = Student('Витя Пчелкин',    1, [random.randint(2, 5) for _ in range(5)])
st2 = Student('Петя Жучков',     1, [random.randint(2, 5) for _ in range(5)])
st3 = Student('Костя Соколов',   1, [random.randint(2, 5) for _ in range(5)])
st4 = Student('Ира Орлова',      2, [random.randint(2, 5) for _ in range(5)])
st5 = Student('Саша Коровкин',   2, [random.randint(2, 5) for _ in range(5)])
st6 = Student('Ваня Перепелкин', 1, [random.randint(2, 5) for _ in range(5)])
st7 = Student('Варя Котова',     1, [random.randint(2, 5) for _ in range(5)])
st8 = Student('Женя Баранов',    2, [random.randint(2, 5) for _ in range(5)])
st9 = Student('Лёха Тонкий',     3, [2, 2, 2, 2, 2])
st10 = Student('Адольф Коган',   3, [5, 5, 5, 4, 6])

st_lst = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
st_lst_tmp = [st.st_info() for st in st_lst]
st_lst = sorted(st_lst_tmp, key=lambda mid_grade: mid_grade[2])
for st in st_lst:
    print(f'{st[0]}, {st[1]}гр. ср.балл: {st[2]}')
