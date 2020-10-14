'''
Escreva uma função que gera uma matriz 4x4 com os números de 0 a 15 sem repetições.
'''
import random
matriz = []


def matriz_generator(matriz):
    lista = list(range(16))
    while len(lista) > 0:
        line = []
        for i in range(4):
            x = random.choice(lista)
            line.append(x)
            lista.remove(x)
        matriz.append(line)


for i in range(4):
    matriz = []
    matriz_generator(matriz)
    print(matriz)