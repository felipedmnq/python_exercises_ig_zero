'''
Dado um número inteiro positivo n, calcular a soma dos n primeiros numeros inteiros positivos.
'''

num = int(input('Digite um número: '))
sum = 0
tot = num
cont = 0
while cont < num:
    sum = sum + tot
    tot -= 1
    cont += 1
print(f'{sum}')