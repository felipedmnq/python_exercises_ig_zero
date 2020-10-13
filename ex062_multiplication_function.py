'''
Escreva uma função que obtenha a multiplicação de vários números de entrada.
'''

def multiplication_f(*num):
    mult_num = 1

    for n in num:
        mult_num *= n

    return mult_num


print(multiplication_f(1, 2, 3, 4))