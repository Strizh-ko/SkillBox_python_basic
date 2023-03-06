class Parents:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info(self):
        print(f'Меня зовут {self.name}. Мне {self.age} лет. Дети: {self.children}')

    def calm_child(self, child_name):
        for i, child in enumerate(self.children):
            if child_name == child.name:
                self.children[i].calm = True
                break

    def feed_child(self, child_name):
        for i, child in enumerate(self.children):
            if child_name == child.name:
                self.children[i].saturation = True
                break


class Children:
    def __init__(self, name, age, calm=False, saturation=False):
        self.name = name
        self.age = age
        self.calm = False
        self.saturation = False

    def info(self):
        print(f'Имя: {self.name}. Лет отроду: {self.age}. Спокойствие: {self.calm}. Сытость: {self.saturation}')


ch1 = Children('Сын', 10)
ch2 = Children('Дочь', 5)
children = [ch1, ch2]
per = Parents('Батя', 50, children)
ch2.info()
per.calm_child('Дочь')
ch2.info()
ch1.info()
per.feed_child('Сын')
ch1.info()
