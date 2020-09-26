'''
Faça um programa que mostre todos os numeros primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar o número de divisões executadas para encontrar os primos.
'''

n = int(input('Digite um valor para N: '))
div = 0
for i in range(1, n + 1):
    prime = True
    j = 2
    while j < i and prime:
        if i % j == 0:
            prime = False
        div += 1
        j += 1
    if prime:
        print(i)
print(f'Foram feitas {div} divisões.')