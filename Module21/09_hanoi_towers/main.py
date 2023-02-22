def move(n, off=1, to=3):
    if min(Hanoi[off]) == n and (len(Hanoi[to]) == 0 or min(Hanoi[to]) > n):
        Hanoi[off].remove(n)
        Hanoi[to].add(n)
        print(f'Перекидываем -={n}=- c {off} на {to}')
        return
    else:
        mid = 6 - (off + to)
        move(n - 1, off, mid)
        move(n, off, to)
        move(n - 1, mid, to)


n = int(input('Введите высоту башни: '))
Hanoi = {1: {i for i in range(1, n + 1)}, 2: set(), 3: set()}

move(n)
