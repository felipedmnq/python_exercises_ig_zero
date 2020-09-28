'''
Entradas - altura e peso.
Calcular peso ideal.
Homens - (72.7*h)-48.
Mulheres - (62.1*h)-44.1
informar se está dentro, acima ou abaixo do peso.
'''
while True:
    sex = input('Sexo [M/F]: ').strip().upper()[0]
    if sex not in 'MF':
        print('Entrada inválida!')
        sex = input('Sexo [M/F]: ').strip().upper()[0]
    else:
        break
height = float(input('Altura (metros): '))
weight = float(input('Peso (kg): '))
ideal_weight = 0

if sex == 'M':
    ideal_weight = (72.7 * height) - 48
elif sex == 'F':
    ideal_weight = (62.1 * height) - 44.1

print(f'Sexo: {sex}.'
      f'\nAltura: {height} M.'
      f'\nPeso: {weight} Kg.'
      f'\nPeso ideal: {ideal_weight:.2f} Kg.')
if weight > ideal_weight:
    print('PESSOA ACIMA DO PESO.')
elif weight < ideal_weight:
    print('PESSOA ABAIXO DO PESO.')
else:
    print('PESSOA ESTÀ NO PESO IDEAL.')