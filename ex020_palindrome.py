'''
N é palindromo se:
    - O 1º algarismo de N é igual ao ultimo algarismo.
    - O 2º algarismo de N é igual ao penúltimo algarismo.
    e assim por diante.

ex: 567765 e 32423 são palíndromos.

Dado um número natural N > 10, verificar se N é palíndromo.
'''

num = int(input('Digite um número menor que 10 para saber se ele é um palíndromo: '))
aux = num
reverse = 0

while aux != 0:
    reverse = reverse * 10 + aux % 10
    aux //= 10
if reverse == num:
    print(f'{num} É PALÍNDROMO.')
else:
    print(f'{num} NÃO É PALÍNDROMO.')