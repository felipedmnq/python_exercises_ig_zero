'''
peça para o usuário entar com o inicio e o fim da tabuada e imprima a tabuada correspondente dentro dos intervalos
correspondentes
'''

init = int(input('Inicio: '))
final = int(input('Final: '))

for c in range(init, final + 1):
    print()
    print(f'TABUADA DO {c}:')
    for i in range(init, final + 1):
        print(f'{c} X {i} = {c * i}')