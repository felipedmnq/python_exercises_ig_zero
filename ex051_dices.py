'''
Simule o lançamento de um dado 100X e armazene em uma lista, mostrar quantas vezes cada valor foi lançado.
'''

from random import randint
dices = []
lounch = int(input('Quantas vezes deseja lançar o dado?: '))
for d in range(lounch):
    dices.append(randint(1, 6))

for c in range(6):
    print(f'O número {c + 1} teve {dices.count(c + 1)} ocorrências, correnpondendo a'
          f' {(dices.count(c + 1) / lounch) * 100:.2f}%.')