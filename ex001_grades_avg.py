'''Faça um programa que peça as 4 notas bimestrais e mostre a média'''

grades = []
for c in range(0, 4):
    n = float(input(f'Nota do {c + 1}º semestre: '))
    grades.append(n)
soma  = sum(grades)
avg = soma / len(grades)
print(f'A média das notas dos 4 semestres é: {avg}')



