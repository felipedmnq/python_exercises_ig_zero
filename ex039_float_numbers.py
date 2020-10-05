'''
faça um programa que peça dois N inteiros e um N real e calcule:
    A) O produto do dobro do primeiro com metade do segundo.
    B) A soma do triplo do primeiro com o terceiro.
    c) O terceiro elevado ao cubo.
'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

calc_a = (num1 * 2) * (num2 / 2)
calc_b = (num1 * 3) + num3
calc_c = num3**3

print(f'resuldados:\n{calc_a}.\n{calc_b}.\n{calc_c}.')