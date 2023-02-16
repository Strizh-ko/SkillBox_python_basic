def minimum(line, tpl):
    return min(len(line), len(tpl))

line = 'abcd'
tpl = (10, 20, 30, 40)

pair = ((line[i], tpl[i]) for i in range(minimum(line, tpl)))

print(pair)
for i in pair:
    print(i)

