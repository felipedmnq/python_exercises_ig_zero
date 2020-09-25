'''
Faça um programa que mostre todos os numeros primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar o número de divisões executadas para encontrar os primos.
'''

n = int(input('Digite um número inteiro: '))
div = soma = 0
for c in range(1, n + 1):
    div += 1
    if n % c == 0:
        print('\033[1;34m', c, end=' \033[m')
        soma += 1
    else:
        print(c, end=' ')
if soma == 2:
    print(f'\n{n} é primo.')
else:
    print(f'\n{n} não é primo.')
print()
print(f'TOTAL DE DIVISOES = {div}')
