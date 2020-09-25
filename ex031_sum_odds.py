'''
Sabe-se que um número da forma n**3 é igual a soma de n ímpares consecutivos.
Dado m, determine os impares consecutivos cuja soma pe igual a n**3 para n assumindo valores de 1 a m.
'''

m = int(input('Digite um número: '))
init = m * (m - 1) + 1


print(f'{m}**3 = {init}', end=' + ')
count = 1
while count < m:
    init += 2
    if count == m - 1:
        print(f'{init} = {m**3}')
    else:
        print(f'{init}', end=' + ')
    count += 1

