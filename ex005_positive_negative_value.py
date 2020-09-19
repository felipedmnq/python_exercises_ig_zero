'''
Faça um progama que peça um valor e informe se ele é positivo ou negativo.
'''

num = float(input('Digite um npumero qualquer: '))
if num < 0:
    print(f'{num} é um valor NEGATIVO.')
elif num > 0:
    print(f'{num} é um valor POSITIVO.')
else:
    print(f'{num} é um valor NULO.')