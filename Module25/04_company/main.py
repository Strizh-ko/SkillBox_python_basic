class Person:
    __pr_list = list()

    def __init__(self, name="name", surname="surname", age=0):
        self.salary = None
        self.__name = name
        self.__surname = surname
        self.__age = age


    def __str__(self):
        return f'{self.get_name()} {self.get_surname()}. З/П: {self.salary}'

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_pr_list(self):
        return self.__pr_list

    def set_pr_list(self):
        self.__pr_list.append(self)

class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def f_salary(self):
        return None


class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = self.f_salary()
        self.set_pr_list()

    def f_salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, name, surname, age, val):
        super().__init__(name, surname, age)
        self.val = val
        self.salary = self.f_salary()
        self.set_pr_list()

    def f_salary(self):
        return 5000 + 0.05 * self.val


class Worker(Employee):

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours
        self.salary = self.f_salary()
        self.set_pr_list()

    def f_salary(self):
        return 100 * self.hours


manag1 = Manager('Константин', 'Волков', 40)
manag2 = Manager('Вася', 'Рогов', 41)
manag3 = Manager('Кира', 'Иванова', 42)
agent1 = Agent('Кристина', 'Козлова', 33, 15000)
agent2 = Agent('Кристофер', 'Нолан', 34, 3000)
agent3 = Agent('Раиса', 'Цыганюк', 38, 1000)
worker1 = Worker('Джон', 'Сноу', 29, 300)
worker2 = Worker('Петр', 'Второй', 28, 200)
worker3 = Worker('Брэд', 'Пинт', 27, 100)

person = Person()
for i in person.get_pr_list():
    print(i)
