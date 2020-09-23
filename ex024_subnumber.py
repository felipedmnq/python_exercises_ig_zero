'''
Dados dois números inteiros positivos P e Q, sendo que o número de digitos de P é menor ou igual ao número de
digitos de Q. Verificar se P é um subnúmero de Q.

EX:
P = 23, Q = 57233, p é subnúmero de Q (P está contido em Q).
'''

p = int(input('Digite um valor "P" com dois digitos: '))
q = int(input('Digite um número "Q" com 5 digitos: '))

# calcula o número de dígitos de P.
aux_p = p
cont_d = 0
while aux_p != 0:
    aux_p //= 10
    cont_d += 1

# comparação entre P e Q.
# P é sub de Q --> paro a execução.
# Q == 0
comparando = True
aux_q = q
while comparando:
    subnum_q = aux_q % (10**cont_d)
    if subnum_q == p:
        comparando = False
    aux_q //= 10
    if aux_q == 0:
        comparando = False
if subnum_q == p:
    print(f'{p} é subnúmero de {q}.')
else:
    print(f'{p} não é subnúmero de {q}')