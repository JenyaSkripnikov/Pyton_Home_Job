# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке.
# Пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

while True:
    try:
        number = int(input('\nВведите число N:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

import random
listfirst = []
for i in range(number):
    listfirst.append(random.randint(-number, number))

print(f'\nСписок из N={number} элементов, заполненных числами из промежутка [-{number}, {number}]:\n{listfirst}')

listsecond = []
for j in range(2):
    listsecond.append(random.randint(0, number))

print(f'\nСписок позиций для произведения элементов:\n{listsecond}')
print(f'\nПроизведение элементов на указанных позициях составляет:\n{listfirst[listsecond[0]] * listfirst[listsecond[1]]}')
