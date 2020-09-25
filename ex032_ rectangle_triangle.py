'''
Dados tres numeros naturais, verificar se eles formam os lados de um triangulo retângulo.

A ** 2 + B ** 2 == C ** 2
C ** 2 + B ** 2 == A ** 2
C ** 2 + A ** 2 == B ** 2
'''

A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))

if A ** 2 + B ** 2 == C ** 2 or C ** 2 + B ** 2 == A ** 2 or C ** 2 + A ** 2 == B ** 2:
    print(f'O triângulo de lados {A}, {B} e {C} é retângulo.')
else:
    print(f'O triângulo de lados {A}, {B} e {C} não é retângulo.')

