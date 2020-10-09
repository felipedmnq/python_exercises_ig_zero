'''
Peça as 04 notas de 10 alunos, armazenar em uma lista a média, imprimir alunos com média maior que 7.
'''
notes     = []
avg_notes = []
alunos    = 10
bigger_seven = 0

for s in range(alunos):
    for n in range(4):
        notes.append(float(input(f'Digite a {n + 1}ª nota do {s + 1}º aluno: ')))
    avg_notes.append(sum(notes) / 4)
    notes.clear()

for n in avg_notes:
    if n >= 7:
        print(f'{bigger_seven} alunos tiveram médias de notas maiores que 7 e as médias são: {n}')
        bigger_seven += 1

print('-' * 30)
print(avg_notes)