'''
Faça um programa que mostre todos os numeros primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar o número de divisões executadas para encontrar os primos.
'''

n = int(input('Digite o valor de N: '))
div = soma = div_tot = 0
for c in range(1, n + 1):
    div += 1
    if n % c == 0:
        print('\033[1;34m', c, end=' \033[m')
        soma += 1
        div_tot += 1
    else:
        print('\033[1;31m',c,'\033[m', end=' ')
if soma == 2:
    print(f'\033[1;33m\n{n} é primo.\033[m')
else:
    print(f'\033[1;31m\n{n} não é primo.\033[m')
print()
print(f'TOTAL DE DIVISOES = {div}.\nTotal de divisões inteiras: {div_tot}.')
