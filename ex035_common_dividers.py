'''
Dados dois numeros inteiros poristivos I e J diferentes de 0, imprimir os divisores comuns de i e j.

ex: I = 2, J = 3 --> saida: 1.
    I = 9, J = 21 --> saida: 1, 3.
'''

i = int(input('Digite um valor para I: '))
j = int(input('Digite um valor para J: '))
'''
for c in range(1, i):
    if i % c == 0:
        print(c, end=' ')
print()
for c in range(1, j):
    if j % c == 0:
        print(c, end=' ')
'''
if i <= j:
    for c in range(1, i):
        if i % c == 0 and j % c == 0:
            print(c, end=' ')
else:
    for c in range(1, j):
        if i % c == 0 and j % c == 0:
            print(c, end=' ')