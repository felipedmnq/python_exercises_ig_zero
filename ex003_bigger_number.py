'''
faça um programa que peça dois numeros e imprima o maior deles.
'''

n1 = int(input('1º número: '))
n2 = int(input('2º número: '))

if n1 > n2:
    print(f'O maior número digitado foi {n1}')
if n2 > n1:
    print(f'O maior número digitado foi {n2}')
else:
    print(f'{n1} e {n2} são iguais.')