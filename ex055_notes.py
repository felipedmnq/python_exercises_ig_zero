'''
leia um numero indeterminado de notas (para em -1).
imprima:
    1 - valores lidos.
    2 - exibirr valores em ordem de inserção.
    3 - em ordem inversa.
    4 - soma dos valores.
    5 - média
    6 - valores acima da média (quantidade).
    7 - qtidade de valores abaixo de 7
    8 - encerre o programa com uma mensagem.
'''
notes = []

while True:
    note = float(input('Nota ([-1] para sair): '))
    if note == -1:
        break
    notes.append(note)

print('-' * 30)
print(f'Foram cadastradas {len(notes)} notas.')
print('As notas cadastradas foram: ', end='')
for nota in notes:
    print(nota, end=', ')

print()
print('Ordem invertida: ', end='')
for nota in reversed(notes):
    print(nota, end=', ')
print()
print(f'A soma das notas digitadas é: {sum(notes)}.'
      f'\nA média das notas digitas foi: {sum(notes) / len(notes)}.')

lower_qtd = 0
upper_qtd = 0
for nota in notes:
    if nota > (sum(notes) / len(notes)):
        upper_qtd += 1
    if nota < 7:
        lower_qtd += 1
print(f'Foram digitadas {upper_qtd} notas acima da média.')
print(f'Foram digitadas {lower_qtd} notas abaixo de 7.')
print('FUI....VALEU!!')