"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5
Segundo Salto: 6.1
Terceiro Salto: 6.2
Quarto Salto: 5.4
Quinto Salto: 5.3

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

jumps = []

name = input('Nome do atleta: ')
print(f'Atleta: {name}.')

for j in range(5):
    jump = float(input(f' - {j + 1}º salto: '))
    jumps.append(jump)

print('-' * 30)
print(f'{"Resultado Final":^30}')
print('-' * 30)
print(f'Atleta: {name}.')
print('Saltos: ', end='')
for j in jumps:
    print(j, end=' - ')
    if j == jumps[-1]:
        print(j)
print(f'Média dos saltos: {sum(jumps) / len(jumps):.2f} m.')


