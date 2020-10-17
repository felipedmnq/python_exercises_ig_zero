'''
Guess Game: The player has to guess a random number between 1 and 100.
'''

import random

cpu = random.randint(1, 100)
plays = 0

print('-' * 40)
print(f'{"GUESS GAME":^40}')
print(f'{"Try to guess the number!":^40}')
print('-' * 40)

while True:
    while True:
        player = int(input('Try to guess the number (1 - 100): '))
        if player not in range(101):
            print('A NUMBER BETWEEN 01 AND 100.')
            player = int(input('Try to guess the number (1 - 100): '))
        else:
            break

    plays += 1

    if player == cpu:
        break
    elif player > cpu:
        print(f'OOPS, {player} is too big, try a lower!!!')
    elif player < cpu:
        print(f'OOPS, {player} is too low, try a bigger!!!')

print(print('-' * 40))

if plays == 1:
    print(f'WOOOOOW, at first shoot, you are GOOD! You won!!')
else:
    print(f'You needed {plays} chances to guess!!')

