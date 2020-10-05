'''
faça um programa que leia um conjunto indeterminado de temperaturas e informe ao final qual a maior e qual a menor
temperatura informados, bem como a média.
'''

num = int(input('Digite o número de temperaturas a ser registradas: '))
sum_temp = bigger_temp = lower_temp = 0

for t in range(num):
    temp = float(input('Temperatura: '))
    sum_temp += temp
    if t == 0:
        bigger_temp = temp
        lower_temp = temp
    if temp > bigger_temp:
        bigger_temp = temp
    if temp < lower_temp:
        lower_temp = temp

print(f'ANÁLISE DE DADOS DAS TEMPERATURAS:'
      f'\nMAIOR TEMPERATURA: \t\t{bigger_temp:6.2f}ºC.'
      f'\nMENOR TEMPERATURA: \t\t{lower_temp:6.2f}ºC.'
      f'\nMÉDIA DE TEMPERATURAS: \t{sum_temp / num:6.2f}ºC.')


