"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""

while True:
    turn = input('Em qual turno você trabalha?'
                 '\nM - Matutino.'
                 '\nV - Vespertino.'
                 '\nN - Noturno.')
    answr = input('Resposta: ').upper().strip()
    if answr in 'MVN':
        break

if answr == 'M':
    print('BOM DIA!')
elif answr == 'V':
    print('BOA TARDE!')
elif answr == 'N':
    print('BOA NOITE!')