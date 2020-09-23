'''
Dados N e uma sequencia de números N inteiros, determinar quantos segmentos de números iguais consecutivos compõem
essa sequência.

ex: 5, 2, 2, 3, 4, 4, 4, 4, 1, 1 = 5 segmentos de números iguais.
'''

num = int(input('Quantos números terá a sequência?: '))
ant = int(input('Digite o 1º número da sequência: '))
cont = 1
segment = 0

while cont < num:
    prox = int(input(f'Digite o {cont + 1}º número da seqência: '))
    if ant == prox:
        segment += 1
    cont += 1
    ant = prox
print()
print(f'Essa sequência possui {segment} segmentos de números iguais.')
