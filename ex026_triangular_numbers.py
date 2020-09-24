'''
triangular = n * (n+1) / 2
escreva um programa que imprima os numeros triangulares com indices multipros de 5 entre 5 e 50.
'''

for n in range(5, 51, 5):
    triangular = n * (n + 1) // 2
    print(f'{n}º número triangular é {triangular}')