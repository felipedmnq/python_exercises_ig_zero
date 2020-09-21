'''
Fatorial - Dado umnúmero inteiro não-negativo n, determinar n!
'''

n = int(input('Digite um valor para saber seu fatorial: '))
fat = 1
cont = n
while cont != 0:
    fat = fat * cont
    cont -= 1
print(f'{n}! = {fat}')