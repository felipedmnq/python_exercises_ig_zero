'''
imprimir a tabuada de 1 até n.
'''

def tabulation(n):
    def multip(x):
        return x*n
    return multip


def main():
    n = int(input('Quantas tabuadas?: '))
    for c in range(1, n + 1):
        f = tabulation(c)
        print(f'TABUADA DO {c}:')
        for i in range(11):
            print(f'{c} X {i} = {f(i):2}')
        print()


main()


