'''
Dizemos que um número inteiro positivo N é perfeito se for igual à soma de seus divisores positivos diferentes de N.
EX: 6 é perfeito => 1 + 2 + 3 = 6

Dado um número inteiro positivo N, verificar se ele é perfeito.
'''

num = int(input('Digite um número para saber se ele é perfeito: '))
#num_list = []
cont = 1
soma = 0

'''
while cont < num:
    if num % cont == 0:
        num_list.append(cont)
    cont += 1
if sum(num_list) == num:
    print(f'{num} é um número PERFEITO.')
else:
    print(f'{num} NÃO É um número perfeito')
'''
while soma < num:
    if num % cont == 0:
        soma += num
    cont += 1
if soma == num:
    print(f'{num} é um número perfeito.')
else:
    print(f'{num} não é um número perfeito.')



