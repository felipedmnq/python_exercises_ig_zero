'''
dizemos que um número natural é triangular se ele é produto de números naturais consecutivos.
ex: 120 é triangular = 4 X 5 X 6 = 120

Dado um n inteiro positivo, verificar se é triangular.
'''

num = int(input('Digite um número para saber se ele é "triangular": '))
n1, n2, n3 = 1, 2, 3

while n1 * n2 * n3 < num:
    n1 += 1
    n2 += 1
    n3 += 1
if n1 * n2 * n3 == num:
    print(f'{num} é um número triangular.')
else:
    print(f'{num} não é triangular.')


