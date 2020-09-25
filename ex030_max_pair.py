'''
Dados dois naturais m e n determinar, entre todos os pares de números naturais (x, y) tais que x < m e y < n,
um par para o qual o valor da expressão x * y - x ** 2 + y seja máximo e calcular também esse maximo.
'''
m = int(input('m: '))
n = int(input('n: '))

x = y = max = x_max = y_max = 0
while x < m and y < n:
    for i in range(m):
        for j in range(n):
            soma = i * j - i ** 2 + j
            print(soma)
            if soma > max:
                max = soma
                x_max = i
                y_max = j
    x += 1
    y += 1
print(f'O valor máximo é {max} para o par (x, y) = ({x_max}, {y_max}).')