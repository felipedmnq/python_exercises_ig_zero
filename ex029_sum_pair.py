'''
Dados N e N sequencias de números inteiros não nulos, cada qual seguida por um 0, calcular a soma dos números pares
de cada sequencia.
'''

n = int(input('Digite o número de sequências: '))

for c in range(n):
    print(f'Sequência {c + 1}.')
    num = int(input('Digite um número da sequência (zero encerra): '))
    sum_pairs = 0
    while num != 0:
        if num % 2 == 0:
            sum_pairs += num
        num = int(input('Digite um número da sequência (zero encerra): '))
    print(f'A soma da sequência {c + 1} é: {sum_pairs}')
    print()
