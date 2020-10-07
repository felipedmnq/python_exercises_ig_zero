'''
leia 20 numeros e int e armazeneos em uma lista, separar por par e impar e mostrar as 3 listas.
'''
from random import randint

numbers = [[],[]]

for n in range(20):
    num = randint(0, 100)
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

print(f'Números sorteados: {numbers}.'
      f'\nPares: {numbers[0]}.'
      f'\nImpares: {numbers[1]}')


