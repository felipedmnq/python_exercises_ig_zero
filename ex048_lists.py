'''
leia 5 numeros inteiros e mostre-os
'''

numbers = []

for n in range(5):
    numbers.append(int(input(f'Digite o {n + 1}º número: ')))

print(numbers)