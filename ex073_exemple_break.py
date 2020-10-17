'''
Escreva uma função que produza a soma dos primeiros n números de uma lista com tamanho M.
'''


def create_list():
    numbers = []

    m = int(input('Tamanho da lista: '))

    for c in range(m):
        element = float(input(f'Elemento {c + 1}/{m}: '))
        numbers.append(element)

    return numbers


def main():
    l1 = create_list()

    n = int(input('Número de elementos que deseja somar: '))

    sum = 0
    for i in range(len(l1)):
        if i == n:
            break
        sum += l1[i]

    print(f'A soma dos elementos é: {sum}.')


main()
