'''
escreva uma função que obtenha o maior número de uma sequência de numeros.
'''

def bigger_num(*num):
    #return max(num)
    bigger = num[0]

    for n in num:
        if n > bigger:
            bigger = n

    return bigger


print(bigger_num(1, 2, 3, 5, 16, 4, 7, 8))