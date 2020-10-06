'''
Teste estatística "qebrando a banca"
'''
import random

test = int(input('Número de testes: '))
change = not_change = 0

for i in range(test):
    door = random.randrange(1, 4)
    prize = random.randint(1, 3)
    if door == prize:
        not_change += 1
    else:
        change += 1

print(f'É vantajoso trocar em {change * 100 / test:.3f}% das vezes.'
      f'\nNão é vantajoso trocar em {not_change * 100 / test:.3f}% das vezes.')