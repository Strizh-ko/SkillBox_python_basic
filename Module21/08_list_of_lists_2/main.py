nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def lists(groups, names=None):
    names = names or []
    flag = True
    for group in groups:
        if isinstance(group, list):
            names.extend(group)
            flag = False
        else:
            names.append(group)
    if flag:
        return print(names)
    return lists(names)

lists(nice_list)