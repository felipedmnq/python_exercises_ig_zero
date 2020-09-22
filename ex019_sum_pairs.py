'''
Dado N e uma sequencia de N números inteiros, determinar a soma dos pares.
'''

num = int(input('Digite um número para saber a soma dos números pares que o antecedem: '))
sum_pair = 0
count = 2
while count < num:
    if count % 2 == 0:
        sum_pair += count
    count += 1
print(f'a soma dos números pares que o antecedem {num} é igual a {sum_pair}')