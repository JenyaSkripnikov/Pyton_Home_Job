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
# print(f'\nСписок из N={number} элементов, заполненных числами из промежутка [-{number}, {number}]:\n{list}')

# listsecond = []
# for j in range(0, number):
#     listsecond.append(random.randint(0, number))

# listresult = []
# for i in list:
#     if i in listsecond:
#         listresult.append(int(i))

# print(f'\n{listsecond}, \n{listresult}')

# print(f'\nСписок позиций для произведения элементов:\n{listsecond}')
# print(f'\n{}')