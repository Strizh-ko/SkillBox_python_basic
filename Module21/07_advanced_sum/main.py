def perfect_sum(*args):
    rez = 0

    if len(args) == 1 and isinstance(args, (tuple, list)):
        args = (num for lst in args for num in lst)

    for num in args:
        if isinstance(num, int):
            rez += num
        elif isinstance(num, str):
            continue
        else:
            rez += perfect_sum(num)
    return rez

print(perfect_sum(1, 2, 3, 4, 5))
print(perfect_sum([[[1, 2, [3]], [1], 3]]))