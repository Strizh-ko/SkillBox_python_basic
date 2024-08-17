def score_key(player):
    return int(player[1][0]), int(player[1][1])

n = int(input('Сколько записей вносится в протокол? '))

registr = dict()
for i in range(n):
    play = input(f'{i + 1}-я запись: ').split()
    if play[1] in registr:
        if int(registr[play[1]][0]) < int(play[0]):
            registr[play[1]] = [int(play[0]), -(i + 1)]
    else:
        registr[play[1]] = [int(play[0]), -(i + 1)]

score_list = list(registr.items())

score_list.sort(key=score_key, reverse=True)
print('\nИтоги соревнований:')
for i in range(3):
    print(f'{i + 1}е место. {score_list[i][0]} ({score_list[i][1][0]})')

