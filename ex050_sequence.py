lista = []
num = int(input('Digite um número: '))

while num != -1:
    lista.append(num)
    num = int(input('Digite um número: '))

element = int(input('Elemento a ser buscado: '))
print(f'O elemento {element} aparece {lista.count(element)} vezes na sequência.')
'''
cont_element = 0

for e in range(len(lista)):
    if lista[e] == element:
        cont_element += 1

print(f'O elemento {element} aparece {cont_element} vezes na sequência.')
'''