'''
Faça um programa para leitura de tres notas parciais de um aluno. O programa deve calcular a média e apresentar:
        Aprovado - se >= 7
        Reprovado - se < 7
        Aprovado com distinção - se = 10.
'''

n1 = float(input('Nota 1º semestre: '))
n2 = float(input('Nota 2º semestre: '))
n3 = float(input('Nota 3º semestre: '))
avg = (n1 + n2 + n3) / 3
print(f'Média: {avg}.')
if avg == 10:
    print('APROVADO COM DISTINÇÃO.')
elif 10 > avg >= 7:
    print('APROVADO.')
else:
    print('REPROVADO.')
