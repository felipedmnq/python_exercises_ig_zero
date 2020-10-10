'''
teste de probabilidade - mega sena (1:50.063.860)
'''

import random

selected = [4, 7, 21, 29, 42, 50]
lotto    = list(range(1, 61))

num = int(input('Número de testes: '))
cont_loop = soma = 0

for t in range(num):
    drawn     = []

    while selected != drawn:
        lotto_selected = lotto.copy()
        drawn = []

        for i in range(6):
            num_selected = random.choice(lotto_selected)
            drawn.append(num_selected)
            lotto_selected.remove(num_selected)

        selected.sort()
        cont_loop += 1
    print(f'Tentativas: {cont_loop}.')

soma /= num
print(f'Média do resultado: {soma}.')

