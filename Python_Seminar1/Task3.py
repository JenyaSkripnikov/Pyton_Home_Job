# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

while True:
    try:
        ordinateX = int(input('\nВведите X:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t')

while ordinateX == 0:
    print('\nЗначение X не должно равняться нулю.')
    ordinateX = int(input('\nВведите X:\t'))

while True:
    try:
        abscissaY = int(input('\nВведите Y:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t') 

while abscissaY == 0: 
    print('\nЗначение Y не должно равняться нулю.')
    abscissaY = int(input('\nВведите Y:\t'))

if int(ordinateX) > 0 and int(abscissaY) > 0:
        print(f'\nX={ordinateX} и Y={abscissaY} -> I четверть')
elif int(ordinateX) < 0 and int(abscissaY) > 0:
        print(f'\nX={ordinateX} и Y={abscissaY} -> II четверть')
elif int(ordinateX) < 0 and int(abscissaY) < 0:
        print(f'\nX={ordinateX} и Y={abscissaY} -> III четверть')
elif int(ordinateX) > 0 and int(abscissaY) < 0:
        print(f'\nX={ordinateX} и Y={abscissaY} -> IV четверть')
