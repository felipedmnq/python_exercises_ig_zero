'''
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que 1 litro de tinta cobre 6 m² de área.
A tinta é vendida em latas de 18l = R$80 e faloes de 4l = R$ 25.

Informe a quantidade de tinta necessária e os preços em 3 situações:
    latas de 18 litros.
    Galoes de 4 litros.
    Misturar latas e galoes ( menor preço ).

Acrescente margem de erro de 10% e valores e litros arredondados para cima (latas cheias - fechadas).
'''

area = float(input('Area a ser pintada (m²): '))
area_error = area * 1.1                        # margem de erro de 10% para mais.
liters = area_error // 6
if area_error % 6 > 0:
    liters += 1

cans = int(liters // 18)
galons = int(liters // 4)

if liters % 4 > 0:
    galons += 1
if liters % 18 > 0:
    cans += 1

cans_price = cans * 80
galons_price = galons * 25

print(f'Para pintar uma área de {area}m² serão necessários {galons} galões de 4 litros '
      f'ou {cans} latas de 18 litros.')
print(f'{galons} galões de 4 litros: R$ {galons_price:.2f}.'
      f'\n{cans} latas de 18 litros: R$ {cans_price:.2f}.')

if galons_price > cans_price:
    print(f'A opção mais barata é comprar a tinta necessária em latas de 18 litros, '
          f'{cans} latas dão um total de R$ {cans_price:.2f}')
else:
    print(f'A opção mais barata é comprar a tinta necessária em galões de 4 litros, '
          f'{galons} galões dão um total de R$ {galons_price:.2f}')
print('go to git')