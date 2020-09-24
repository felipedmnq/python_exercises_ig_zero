'''
Em uma eleição existem 3 candidatos, faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

voters = int(input('Número de eeleitores: '))
candidate1 = candidate2 = candidate3 = 0
for c in range(0, voters):
    vote = int(input(f'{c+1}º Eleitor - Em qual candidato deseja votar (1, 2 ou 3)?: '))
    if vote == 1:
        candidate1 += 1
    elif vote == 2:
        candidate2 += 1
    elif vote == 3:
        candidate3 += 1
    else:
        print('VOTO INVÁLIDO, ESSE CANDIDATO NÃO EXISTE!')
print(f'Candidato 01 = {candidate1}.\nCandidato 02 = {candidate2}.\nCandidato 03 = {candidate3}.')
