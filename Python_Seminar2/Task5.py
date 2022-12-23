# Реализуйте алгоритм перемешивания списка. 
# (рандомно поменять местами элементы списка между собой)

while True:
    try:
        number = int(input('\nВведите кол-во элементов списка:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

import random
list = []
for i in range(1, number + 1):
    list.append(int(i))
    
print(f'\nПервоначальный список:\n{list}')
random.shuffle(list)
print(f'\nИзменённый список:\n{list}')
