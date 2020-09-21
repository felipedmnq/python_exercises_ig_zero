'''
Dada uma sequencia de numeros inteiros não nulos seguida por 0, imprimir seus quadrados.
'''

while True:
    num = int(input('Digite um número para saber seu quadrado (0 para sair): '))
    if num == 0:
        print('Programa finalizado.')
        break
    else:
        print(f'{num} ao quadrado = {num * num}')
