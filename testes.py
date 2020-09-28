n = int(input('N: '))
soma = 0.0

for i in range(1, n+ 1):
    soma += i / (n - i + 1)
print(f'A soma vale: {soma}.')