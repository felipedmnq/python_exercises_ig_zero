'''
Dado um número inteiro positivo n, imprimir os n primeiros numeoros naturais impares.
'''

num = int(input('Digite um número inteiro positivo: '))
cont = 0
while cont <= num:
    if cont % 2 == 1:
        print(cont, end=' ')
    cont += 1