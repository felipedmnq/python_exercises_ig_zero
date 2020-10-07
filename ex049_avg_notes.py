'''
leia 4 notas e mostra a média entre elas.
'''

notes = []

for n in range(4):
    notes.append(float(input(f'Nota do {n + 1}º aluno: ')))

agv_notes = sum(notes) / len(notes)

print(f'A média das notas entre os {len(notes)} alunos é: {agv_notes:.2f}.')