'''
Dado N e uma sequencia de N npumeros inteiros, determinar o comprimento de um segmento crescente de comprimento máximo.

ex:
Na sequência: 5, 10, 3, 2, 4, 7, 9, 8, 5.
O comprimento do segmento crescente é 4.
10 > 5? --> seg += 1
3 > 10? --> parou. seg -= 1
2 > 3?  --> parou. parou
4 > 2?  --> seg += 1
'''

num = int(input('Digite o tamanho da sequência: '))
print('-' * 40)
ant = int(input('Digite o 1º número da sequência: '))
segment = segmentMAX = cont = 1


while cont < num:
    prox = int(input(f'Digite o {cont + 1}º número da sequência: '))
    if prox > ant:
        segment += 1
    else:
        if segment > segmentMAX:
            segmentMAX = segment
        segment = 1
    cont += 1
    ant = prox
print(f'O maior segmento crescente da sequência é: {segmentMAX}.')

