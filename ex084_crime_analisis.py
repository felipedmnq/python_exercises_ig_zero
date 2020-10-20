"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
count_answr = 0
while True:
    qstn01 = input('Telefonou para a vítima? [S/N]: ').upper()
    if qstn01 not in 'SN':
        qstn01 = input('Telefonou para a vítima? [S/N]: ').upper()
    if qstn01 == 'S':
        count_answr += 1
        if qstn01 in 'SN':
            break

while True:
    qstn05 = input('Esteve no local do crime? [S/N]: ').upper()
    if qstn05 not in 'SN':
        qstn05 = input('Esteve no local do crime? [S/N]: ').upper()
    if qstn05 == 'S':
        count_answr += 1
    if qstn05 in 'SN':
        break


while True:
    qstn02 = input('Mora perto da vítima? [S/N]: ').upper()
    if qstn02 not in 'SN':
        qstn02 = input('Mora perto da vítima? [S/N]: ').upper()
    if qstn02 == 'S':
        count_answr += 1
    if qstn02 in 'SN':
        break

while True:
    qstn03 = input('Devia para a vítima? [S/N]: ').upper()
    if qstn03 not in 'SN':
        qstn03 = input('Devia para a vítima? [S/N]: ').upper()
    if qstn03 == 'S':
        count_answr += 1
    if qstn03 in 'SN':
        break


while True:
    qstn04 = input('Já trabalhou com a vítima [S/N]: ').upper()
    if qstn04 not in 'SN':
        qstn04 = input('Já trabalhou com a vítima [S/N]: ').upper()
    if qstn04 == 'S':
        count_answr += 1
    if qstn04 in 'SN':
        break


print(count_answr)
print('-' * 30)
if count_answr < 2:
    print('INOCENTE.')
elif count_answr == 2:
    print('SUSPEITO.')
elif 2 < count_answr <= 4:
    print('CUMPLICE.')
elif count_answr == 5:
    print('CULPADO.')