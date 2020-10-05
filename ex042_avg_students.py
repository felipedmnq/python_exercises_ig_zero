'''
faça um programa que calcule a média de alunos por turma.
Para isso, peça a quantidade de turmas e a quantidade de alunos para cada turma.
as turmas não podem ter mais de 40 alunos.
'''

classes = int(input('Quantidade de turmas: '))
sum_students = 0

for c in range(classes):
    amount = int(input(f'Número de alunos da {c + 1}ª turma: '))

    while amount < 0 or amount > 40:
        print('\033[1;31mQuantidade de alunos inválida!\033[m')
        amount = int(input(f'Número de alunos da {c + 1}ª turma: '))
    sum_students += amount

print(f'A média dos alunos é {sum_students / classes:.2f}')