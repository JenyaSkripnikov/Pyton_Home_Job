# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

while True:
    try:
        number = int(input('\nВведите число N:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

print(f'\nДля набора чисел:')
for i in range(1, number + 1): 
    print(i, end= ' ')

print(f'\nНабор произведений чисел от 1 до {number} составляет:')
rezult = 1
for i in range(1, number + 1):
    rezult *=i
    print(rezult, end= ' ')