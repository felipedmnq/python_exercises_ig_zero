'''
Receba um número X e devolve o primeiro indice que contenha X. Caso X nao esteja na lista, informe.
'''

numbers = [1, 2, 3, 4, 5, 6, 7]

x = int(input('Valor de X: '))
'''
found = False
indice = 0

while not found and indice < len(numbers):
    if numbers[indice] == x:
        found = True
        print(f'O elemento "{x}" está localizado no índice {indice}.')
    indice += 1

if not found:
    print(f'O elemento "{x}" não pertence a lista.')
'''

if x in numbers:
    print(f'O elemento "{x}" está no indice {numbers.index(x)}.')
else:
    print(f'O elemento "{x}" não pertence a lista.')