# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
# для всех значений предикат.

while True:
    numX = input('\nВведите X, число 0 или 1:\t')
    if not numX.isdigit() or not -1 < int(numX) < 2:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова.')
    elif -1 < int(numX) < 2:
        break 
while True:
    numY = input('\nВведите Y, число 0 или 1:\t')
    if not numY.isdigit() or not -1 < int(numY) < 2:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова.')
    elif -1 < int(numX and numY) < 2:
        break 
while True:
    numZ = input('\nВведите Z, число 0 или 1:\t')
    if not numZ.isdigit() or not -1 < int(numZ) < 2:
        print('\nБыл введен не удовлетворяющий условиям параметр.\nПопробуйте снова.')
    elif -1 < int(numX and numY and numZ) < 2:
        break 

resultfirst = not(numX or numY or numZ)
resultsecond = not numX and not numY and not numZ
result = resultfirst == resultsecond
print(f'\nУтверждения ¬({numX} ⋁ {numY} ⋁ {numZ}) = ¬{numX} ⋀ ¬{numY} ⋀ ¬{numZ}, является {result}.')