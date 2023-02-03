violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time = 0
n = int(input("Сколько песен выбрать? "))

for i in range(n):
    song = input(f"Название {i + 1}-й песни: ")
    for i in violator_songs:
        if song in i:
            i_song = violator_songs.index(i)
            time += violator_songs[i_song][1]

print('\nОбщее время звучания песен:', round(time, 2))