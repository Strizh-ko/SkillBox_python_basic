shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item = input("Название детали: ")

count = 0
price = 0
for i in shop:
    if item == i[0]:
        count += 1
        price += i[1]

print('Кол-во деталей —', count)
print('Общая стоимость —', price)