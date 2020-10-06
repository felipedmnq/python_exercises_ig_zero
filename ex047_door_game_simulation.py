'''
Simulador de jogo das portas.

Olá, bem vindo ao jogo das portas, vamos ver se você ganhará um carro ou não!
Escolha uma porta: X
Você escolheu a porta X, mas eu lhe informo que na porta Y há um bode.
Deseja trocar de porta? (s/n): X
Ganhou um carro!
'''
import random

door = int(input('Escolha uma porta entre 1 e 3: '))
prize = random.randrange(1, 4)
goat = 0

if door and prize != 1:
    goat = 1
elif door and prize != 2:
    goat = 2
else:
    goat = 3

while True:
    choice = input(f'Você escolheu a porta {door}, mas eu lhe digo que na porta {goat} há'
                   f'um bode, deseja trocar de porta? [S/N]: ').upper().split()[0]
    if choice in 'SN':
        break
if choice == 'S':
    if door and goat != 1:
        door = 1
    elif door and goat != 2:
        door = 2
    else:
        door = 3
if door == prize:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')



print(prize)