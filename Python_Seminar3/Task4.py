# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

while True:
    try:
        number = int(input('\nВведите число:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

bin_number = bin(number)
print(f'\nДесятичное число {number} в двоичной системе:\t{bin_number}')