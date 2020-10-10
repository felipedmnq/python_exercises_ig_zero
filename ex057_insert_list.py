'''
Dado a posição "I" inserir o elemmento "X" na posição indicada.
'''

numbers = [1, 2, 3, 4, 6, 7, 8, 9]
print(numbers)

pos = int(input('Posição: '))
element = int(input('Elemento: '))
numbers.insert(pos, element)

print(numbers)