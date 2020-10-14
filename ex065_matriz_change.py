matriz = []
m = int(input('Número de linhas: '))
n = int(input('Número de colunas: '))


def build_matriz(m, n, matriz):
    for i in range(m):
        linha = []
        for j in range(n):
            x = int(input(f'Elemento [{i}, {j}] da matriz:'))
            linha.append(x)

        matriz.append(linha)


def change_matriz(pos1, pos2, matriz):
    element1 = matriz[pos1//10 - 1][pos1 % 10 - 1]
    element2 = matriz[pos2//10 - 1][pos2 % 10 - 1]
    matriz[pos1//10 - 1][pos1 % 10 - 1] = element2
    matriz[pos2//10 - 1][pos2 % 10 - 1] = element1


build_matriz(m, n, matriz)
print(matriz)
pos1 = int(input('Posição do elemento 01: '))
pos2 = int(input('Posição do elemento 02: '))
change_matriz(pos1, pos2, matriz)
print(matriz)