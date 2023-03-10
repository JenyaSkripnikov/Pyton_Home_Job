# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, 
# это нормально и особенность данного языка программирования. 
# ваш ответ может не совпадать с примером(может получитя 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

while True:
    try:
        number = int(input('\nВведите кол-во элементов списка:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

import random
list = []
for i in range(number):
    list.append(random.randint(0, 1000)/100)

print(f'\nCписок:\n{list}')

templist = []
tail = 0
for i in range(number):
    tail = list[i] % 1
    templist.append(tail)

diff = max(templist) - min(templist)
print(f'\nPазница между максимальным и минимальным значением')
print(f'\nдробной части элементов в списке, составляет:\t{round(diff, 2)}')
