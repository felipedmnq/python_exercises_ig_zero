'''
faça um programa que leia um número inteiro menor que 1000 e imprima quantas centenas, dezenas e unidades tem.
    observando os termos no plural e colocando "e", virgula, entre outros.
'''
num = int(input('Digite um valor menor que 1000: '))
if 1000 > num > 100:
    cent = num // 100
    ten = (num % 100) // 10
    dez = (num - (cent * 100))
    un = (num - (cent * 100)) - (ten * 10)
    if num % 100 == 0:
        if num  == 100:
            print(f'{num} = {cent} centena.')
        else:
            print(f'{num} = {cent} centenas.')
    elif num == 111:
        print(f'{num} = {cent} centena, {ten} dezena e {un} unidade.')
    elif num % 100 < 10:
        if num % 100 == 1:
            print(f'{num} = {cent} centenas e {un} unidade.')
        else:
            print(f'{num} = {cent} centenas e {un} unidades.')
    elif dez % 10 == 0:
        if 100 < num < 200:
            print(f'{num} = {cent} centena e {ten} dezenas.')
        elif num == 110:
            print(f'{num} = {cent} centena e {ten} dezena.')
        else:
            print(f'{num} = {cent} centenas e {ten} dezenas.')
    else:
        print(f'{num} = {cent} centenas, {ten} dezenas e {un} unidades.')
elif num <= 100:
    ten = num // 10
    un = num - ten * 10
    if num == 10:
        print(f'{num} = {ten} dezena.')
    elif num % 10 == 0:
        print(f'{num} = {ten} dezenas.')
    elif num <= 10:
        if num == 1:
            print(f'{num} = {un} unidade.')
        else:
            print(f'{num} = {num} unidades')
    else:
        if 10 < num < 20:
            print(f'{num} = {ten} dezena e {un} unidade.')
        elif num % 10 == 1:
            print(f'{num} = {ten} dezenas e {un} unidade.')
        else:
            print(f'{num} = {ten} dezenas e {un} unidades.')
else:
    print('Valor inválido.')
