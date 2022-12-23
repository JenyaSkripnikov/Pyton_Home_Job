# Задайте список из n чисел последовательности (1+1/n)**n 
# и выведите на экран их сумму.

while True:
    try:
        number = int(input('\nВведите число N:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nВведите число:\t')

listrezult = []
rezult = 0
for i in range(1, number + 1):
    rezult = round((1+1/i)**i, 2)
    listrezult.append(float(rezult))

print(f'\nСписок из n={number} чисел последовательности (1+1/n)**n: {listrezult}\nСумма составляет {sum(listrezult)}')
