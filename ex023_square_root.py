'''
Qualquer número natural de 4 algarísmos pode ser dividido em duas dezenas formadas pelos seus 2 primeiros e 2 ultimos digitos

ex:
1297: 12 e 97

Escreva um programa que imprime todos os milhares (4 algarísmos) cuja raiz quadrada seja a soma das dezenas formados pela divisão acima.

ex:
raiz de 9801 = 99 --> 98 + 01.
'''

num = 1000

while num < 10000:
    aux = num
    dois_ultimos = num % 100
    aux //= 100
    dois_primeiros = aux % 100
    if (dois_ultimos + dois_primeiros)**2 == num:
        print(f'{num}')
    num += 1
