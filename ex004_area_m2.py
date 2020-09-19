'''
Faça um programa para uma loja de tintas:

Pedir o tamanho em m2 da area a ser pintada.
1 Lt de tinta para 3 m² de area pintada.
lata de 18 lt de tinta = R$80,00

informar a quantidade de tinta necessária e o preço que será gasto
'''

lenght = float(input('Comprimento da parede (m): '))
height = float(input('Altura da parede (m): '))
title = '          CALCULADORA DE TINTA          '
area = lenght * height
liters = area // 3
if area % 3 > 0:
    liters += 1
cans = liters // 18
if liters % 18 > 0:
    cans += 1
cansPrice = 80

print('-' * len(title))
print(title)
print('-' * len(title))
print(f'Comprimento da parede (m): {lenght}.'
      f'\nAltura da parede (m): {height}.'
      f'\nÁrea da parede (m²): {area}.'
      f'\nTinta necessária (litros): {liters:.2f}.'
      f'\nLatas necessárias (18 litros): {cans}.'
      f'\nValor a pagar: R$ {cans * cansPrice:.2f}')
print('-' * len(title))

