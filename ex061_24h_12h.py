def print_hour(hour, min):
    if hour < 12:
        print(f'{hour}:{min} A.M.')
    elif hour >= 12:
        if hour != 12:
            hour -= 12
        print(f'{hour}:{min} P.M.')


while True:
    while True:
        hour = int(input('Hora: [HH:]: '))
        if 00 <= hour <= 23:
            break
    while True:
        min = int(input('Minuto [:MM]: '))
        if 00 <= min <= 59:
            break
    print_hour(hour, min)
    while True:
        cont = input('Deseja continuar convertendo [S/N]: ').upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
