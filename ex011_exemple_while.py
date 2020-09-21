'''
faça um programa que peça dois numeros, base e expoente, calcule e mostre o primeiro numero elevado ao segundo número,
sem usar a função potência.
'''

base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))
cont = 0
prod = 1
while cont < expoente:
    prod = prod * base
    cont += 1
print(f'{base}^{expoente} = {prod}')
