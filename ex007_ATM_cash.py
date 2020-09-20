'''
Programa simula caixa eletrônico.

O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão entregues.
As notas disponíveis são: R$ 1, 5, 10, 50 e 100.
O valor mínimo é R$10, maximo R$600
O programa não deve se preocupar com as notas existentes na maquina.
'''
msg = '      ATM do Felipe      '
print('\033[1;34m-' * len(msg))
print(msg)
print('-' * len(msg))
print('Mínimo R$ 10,00\nMáximo R$ 600,00')
print('-' * len(msg))
while True:
    value = int(input('\033[1;33mValor do saque: R$ \033[m'))
    if value < 10 or value > 600:
        print('\033[1;31mVALOR INVÁLIDO.\033[m')
    else:
        break
print(f'\033[1;31mO valor solicitado foi R$ {value},00')
print('\033[1;34m-\033[m' * len(msg))
tot = value
ced = value // 100
rest = value % 100
if ced > 0:
    print(f'\033[1;32mTotal de {ced} cédulas de R$ 100,00.')
ced = rest // 50
rest %= 50
if ced > 0:
    print(f'Total de {ced} cédulas de R$ 50,00.')
ced = rest // 20
rest %= 20
if ced > 0:
    print(f'Total de {ced} cédulas de R$ 20,00.')
ced = rest // 10
rest %= 10
if ced > 0:
    print(f'Total de {ced} cédulas de R$ 10,00.')
ced = rest // 5
rest %= 5
if ced > 0:
    print(f'Total de {ced} cédulas de R$ 5,00.')
ced = rest // 1
if ced > 0:
    print(f'Total de {ced} cédulas de R$ 1,00.')

