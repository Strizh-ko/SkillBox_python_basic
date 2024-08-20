def slicer(tuple, a):
    if tuple.count(a) == 1:
        return tuple[tuple.index(a):]
    elif tuple.count(a) == 0:
        return ()
    else:
        return tuple[tuple.index(a):tuple.index(a, tuple.index(a)+1) + 1]
