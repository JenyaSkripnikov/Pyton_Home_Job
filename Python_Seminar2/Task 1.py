# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

while True:
    try:
        number = float(input('\nВведите число:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

n = str(number)
search = []
digit = "0123456789"
for i in n:
    if i in digit:
        search.append(int(i))

print(f'\nДля числа {str(number)}, cумма цифр составляет:\t {sum(search)}')