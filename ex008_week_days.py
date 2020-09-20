'''
faça um programa que leia um número e exiba o dia da semana correspondente.
'''
check = False               # o check informa se o valor foi digitado e possibilita a condicional (if) futura.
day = int(input('Dia da semana: '))
if day == 1:
    print('Domingo.')
    check = True
if day == 2:
    print('Segunda.')
    check = True
if day == 3:
    print('Terça.')
    check = True
if day == 4:
    print('Quarta.')
    check = True
if day == 5:
    print('Quinta.')
    check = True
if day == 6:
    print('Sexta.')
    check = True
if day == 7:
    print('Sábado')
    check = True
if check != True:
    print('Valor inválido!')
