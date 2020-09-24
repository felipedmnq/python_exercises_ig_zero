'''
Calcule o n!
'''

num = int(input('Digite o valor de N: '))
factorial = 1
for c in range(num, factorial - 1, -1):
    factorial *= c
    if c != 1:
        print(f'{c} X ', end='')
    else:
        print(f'{c} = {factorial}')
print(f'{num}! = {factorial}')