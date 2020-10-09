'''
Jogo simples de ataque e cura.
'''
import random

player_life = 500
player_sp   = 100
enemy_life  = 50

enemies_number = int(input('Digite o número de inimigos: '))

enemies = []

for i in range(enemies_number):
    enemies.append([i + 1, enemy_life])

playing = True
while playing:
    print(f'Vida: {player_life}.\nSP: {player_sp}.')
    atack = int(input('1 - Atacar.\n2 - Curar.'))

    if atack == 1:
        select = random.choice(enemies)
        damage = random.randint(10, 15)
        print(f'Causou {damage} de dano no inimigo {select[0]}!')
        select[1] -= damage
        if select[1] <= 0:
            print(f'O inimigo {select[0]} MORREU!')
            enemies.remove(select)
    else:
        if player_sp >= 10:
            cure = random.randint(10, 15)
            print(f'Você recebeu {cure} de vida!')
            player_life += cure
            player_sp -= 10
        else:
            print('SP insuficiente!')

    for enemy in enemies:
        score = bool(random.choice([1, 1, 1, 0]))  # 0 == False; 1 == True.
        if score:
            damage = random.randint(1, 3)
            print(f'O inimigo {enemy[0]} causou {damage} de dano.')
            player_life -= damage
        else:
            print(f'O inimigo {enemy[0]} errou o ataque!')

    if player_sp < 100:
        player_sp += 3
    if player_sp > 100:
        player_sp = 100

    if player_life <= 0:
        print('VOCÊ FOI DERROTADO! FIM DE JOGO!')
        playing = False
