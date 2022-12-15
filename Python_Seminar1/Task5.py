# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

while True:
    try:
        ordinateXA = int(input('\nВведите X координату точки А:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t')
while True:
    try:
        abscissaYA = int(input('\nВведите Y координату точки А:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t')
while True:
    try:
        ordinateXB = int(input('\nВведите X координату точки B:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t')
while True:
    try:
        abscissaYB = int(input('\nВведите Y координату точки B:\t'))
        break
    except ValueError:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова:\t')

ordinateX = round((ordinateXA - ordinateXB)**2, 2)
abscissaY = round((abscissaYA - abscissaYB)**2, 2)
hypothenuse = round((ordinateX + abscissaY)**0.5, 2)
print(f'\nРасстояние между точками А ({ordinateXA}, {abscissaYA}) и B ({ordinateXB}, {abscissaYB})')
print(f'\nсоставляет {hypothenuse}')
