import random

rand_list = [random.randint(0, 10) for _ in range(10)]
print("Оригинальный список:", rand_list)
new_list = [(num, rand_list[i+1]) for i, num in enumerate(rand_list) if i % 2 == 0]
print('Новый список:', new_list)