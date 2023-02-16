def tpl_sort(tpl):
    tpl_list = [i for i in sorted(list(tpl)) if int(i) == i]
    if len(tpl) == len(tpl_list):
        return tuple(tpl_list)
    else:
        return tpl

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
