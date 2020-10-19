fac = int(input('factorial of which number?: '))
factorial = 0
print(f'{fac}! = ', end=' ')
print(f'{fac}', end=' . ')
for n in range(fac):
    if fac != 2:
        print(f'{fac - 1}', end=' . ')
        fac -= 1
print(f'{"1 = "}', end=f'{}')
