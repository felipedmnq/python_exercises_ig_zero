'''
leia dez conjuntos de dois valores (número do aluno e sua altura em cm).
Encontre o aluno mais alto e mais baixo.
Mostre o número do aluno mais alto e mais baixo com sua altura.
'''

bigger = lower = num = num_bigger = num_lower = 0

for n in range(10):
    num = n + 1
    height = float(input(f'Altura do aluno {num}, em centímetros: '))
    if num == 1:
        lower = bigger = height
    elif height > bigger:
        bigger = height
        num_bigger = num
    elif height < lower:
        lower = height
        num_lower = num

print(f'O aluno mais alto é o nº{num_bigger}, com {bigger} cm.'
      f'\nO aluno mais baixo é o nº{num_lower}, com {lower} cm.')