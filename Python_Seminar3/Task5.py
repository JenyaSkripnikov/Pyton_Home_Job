# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

while True:
    try:
        number = int(input('\nВведите кол-во элементов списка:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

list = []
firstbib = 1
secondfib = 0
for i in range(number):
    if i < number:
        sumfib = firstbib + secondfib
        list.append(int(sumfib))
        firstbib = secondfib
        secondfib = sumfib
        i =+ 1

uturn =  list
uturn.reverse()
negativelist = [ -j for j in uturn]

list = []
firstbib = 1
secondfib = 0
for i in range(number):
    if i < number:
        sumfib = firstbib + secondfib
        list.append(int(sumfib))
        firstbib = secondfib
        secondfib = sumfib
        i =+ 1
   
list.insert(0, 0)

unitedlist = negativelist + list
print(f'\nСписок чисел Фибоначчи:\t{unitedlist}')