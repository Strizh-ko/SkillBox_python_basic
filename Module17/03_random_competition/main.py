import random

command_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
command_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

print('Первая команда:', command_1)
print('Вторая команда:', command_2)

winners = [command_1[i] if command_1[i] >= command_2[i] else command_2[i] for i in range(20)]

print('Победители тура:', winners)