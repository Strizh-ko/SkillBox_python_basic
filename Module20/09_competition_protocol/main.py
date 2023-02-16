n = int(input('Сколько записей вносится в протокол? '))


players = []
points = []
for i in range(n):
    play = input(f'{i + 1}-я запись: ').split()
    players.append(play[1])
    points.append(int(play[0]))

print('\nИтоги соревнований:')
for i in range(1,4):
    top_points = max(points)
    winer = players[points.index(top_points)]
    print(f'{i}е место. {winer} ({top_points})')
    players.remove(winer)
    points.remove(top_points)
