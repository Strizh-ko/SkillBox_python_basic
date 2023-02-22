def minimum(*args):
    return min(map(len, args))

def new_zip(*args):
    return [tuple(obj[i] for obj in [list(block) for block in args]) for i in range(minimum(args))]



tpl = ([11, 22, 33], [44, 55, 66], [77, 88, 99])
lst = [10, 20, 30, 40, 50, 60]
dct = {1: 15, 2: 25, 3: 35, 4: 45}

print(new_zip(dct, tpl, lst))