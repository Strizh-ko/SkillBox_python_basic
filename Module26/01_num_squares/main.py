class Square_iter:

    def __init__(self, n: int):
        self.n = n
        self.cur_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cur_num += 1
        if self.cur_num > self.n:
            raise StopIteration()
        return self.cur_num ** 2


def square_gen(n: int):
    for i in range(1, n+1):
        yield i ** 2


n = int(input('Введите число n: '))

way1 = Square_iter(n)
for i in way1:
    print(i, end=' ')

print()

way2 = square_gen(n)
for i in way2:
    print(i, end=' ')

print()

way3 = (i ** 2 for i in range(1, n + 1))
for elem in way3:
    print(elem, end=' ')