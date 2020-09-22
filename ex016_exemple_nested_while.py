'''
Dado um número n de empresas, e um numero m de meses, e o ganho e gastos positivos e inteiros de cada empresa para cada
mes, imprimir se a empresa nesses meses ficou com defict, lucro, ou indiferente e o valor correspondente.
'''
comp = int(input('Digite o número de empresas a ser analisado: '))
month = int(input('Digite o número de meses a serem analisados: '))
emp = 1

while emp <= comp:
    mes = 1
    status = 0
    print(f'Empresa {emp}.')
    while mes < month:
        profit = int(input(f'Lucro da empresa no {mes}º mês: R$ '))
        expenses = int(input(f'Despesas da empresa no {mes}º mês: R$'))
        status += profit - expenses
        print()
        mes += 1
    if status == 0:
        print(f'\033[1;33mA empresa {emp} ficou INDIFERENTE.\033[m')
    elif status > 0:
        print(f'\033[1;34mA empresa {emp} ficou no AZUL - R$ {status:.2f}\033[m')
    else:
        print(f'\033[1;31mA empresa {emp} ficou no VERMELHO - R$ {status:.2f}\033[m')
    emp += 1