'''
Escreva uma função de potenciação.
'''

def potencia(base, expoente):
    pot = base**expoente

    return pot


def soma(num1, num2, num3):
    return num1 + num2 + num3


def opMat(num1, num2):
    soma = num1 + num2
    return soma, num1 * num2


import random
def sorteio_dado():
    return print(random.randint(1, 6))


sorteio_dado()