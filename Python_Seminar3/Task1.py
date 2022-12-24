# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

while True:
    try:
        number = int(input('\nВведите кол-во элементов списка:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

import random
list = []
for i in range(number):
    list.append(random.randint(-10, 10))

print(f'\nСписок:\n{list}')

nechetlist = []
for j in range(number):
    if j %2 != 0:
        nechetlist.append(list[j])
        
print(f'\nСписок элементов стоящих на нечётной позиции:\n{nechetlist},сумма которых составляет: {sum(nechetlist)}')