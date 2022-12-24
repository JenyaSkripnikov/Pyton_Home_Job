# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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

print(f'\nПервоначальный список:\n{list}')

firstlist = []
import math
half = math.ceil(number/2)
for i in range(0, int(half)):
    firstlist.append(list[i])

list.reverse()

secondlist = []
import math
half = math.ceil(number/2)
for i in range(0, int(half)):
    secondlist.append(list[i])

rezultlist = []
count = 0
for i in range(len(firstlist)):
    if i in range(len(secondlist)):
        count = firstlist[i] * secondlist[i]
        rezultlist.append(count)
        i += 1

print(f'\nCписок произведений пар чисел:\n{rezultlist}')
