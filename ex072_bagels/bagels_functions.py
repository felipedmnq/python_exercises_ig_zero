import random

ult_dig = (lambda x: x%10)


def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida
    False --> Entrada Inválida
    """
    if 1000 <= num < 10000:
        return True
    else:
        return False



def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    OBS: O NUMERO NAO PODE TER DIGITOS REPETIDOS
    """
    numbers = list(range(10))
    secretNum = 0

    while numbers[0] == 0:
        random.shuffle(numbers)

    for i in range(4):
        digit = numbers[i]
        secretNum = digit * (10 ** (3 - i))

    return secretNum, numbers[:4]


def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o número escolhido e o número secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Código
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi

    Retorna uma lista vazia caso os dois números sejam iguais
    """
    global ult_dig
    if secretNum == num:
        return []

    dica = []

    for i in range(4):
        if ult_dig(num) == ult_dig(secretNum):
            dica.append(2)
        elif ult_dig(num) in secretNumList:
            dica.append(1)

        num //= 10
        secretNum //= 10

    if len(dica) == 0:
        dica.append(0)

    dica.sort()

    return dica