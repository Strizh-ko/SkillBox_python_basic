def func(line, tpl):
    pair = zip(line, tpl)
    return pair


line = 'abcd'
tpl = (10, 20, 30, 40)

print(func(line, tpl))
for i in func(line, tpl):
    print(i)

