'''
faça um program que leia um numero e informe se ele é inteiro ou decimal.
Se for decimal, arredonde o número.
'''

num = float(input('Digite um número: '))

if num != int(num):
    decimal = num - int(num)
    rounded = int(num)

    if decimal >= 0.5:
        rounded += 1

    print((f'{num} é decimal.'))
    print(f'Arredontando: {rounded}.')
else:
    print(f'{num} é inteiro.')

print('-' * 3)
print(round(num))