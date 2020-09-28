'''
Calcular raizes da equação de 2º grau - ax2 + bx + c.
pedir A, B, C.
informar:
    Se A == 0, não é equação de 2º grau. Não pedir demais valores.
    Se delta for negativo, nao possui raizes reais - informar e encerrar.
    Se delta for == 0 possui apenas uma raiz - informar.
    Se delta for positivo - informar as raizes.

    delta = b**2 - 4*a*c
    raiz = (-b +- (delta)**1/2) (2*a)
'''

a = float(input('Informe o valor de A: '))
if a == 0:
    print(f'A variável A sendo 0, não caracteriza uma equação de 2º grau.')
else:
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    delta = b ** 2 - 4 * a * c
    raiz_pos = float(-b + (delta) ** 1 / 2) / (2 * a)
    raiz_neg = float(-b - (delta) ** 1 / 2) / (2 * a)
    if delta < 0:
        print('Delta possui valor negativo, por esse motivo a equação não possui raizes reais.')
    elif delta == 0:
        print(f'Delta = {delta} possui apenas uma raiz: {raiz_pos}')
    else:
        print(f'As raizes da equação são: {raiz_pos} e {raiz_neg}.')
