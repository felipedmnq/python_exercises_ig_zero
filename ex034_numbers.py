'''
dados N e dois numeros inteiros positivos i e j diferentes de 0, imprimir em ordem crescente os N primeiros naturais
que são multiplos de i ou j ou ambos.

ex: n = 6 --> i = 2 e j = 3 a saida sera: 0, 2, 3, 4, 6, 8.
'''
n = int(input('Digite um valor para N: '))
i = int(input('Digite um valor para I: '))
j = int(input('Digite um valor para J: '))

cont = 0

while cont <= n:
    if cont % i == 0 or cont % j ==0:
        print(cont, end=' ')
    cont += 1