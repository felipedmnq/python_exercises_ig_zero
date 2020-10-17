numbers = [
    326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
    1, 7, 16
]

for num in numbers:
    hundreds = num // 100
    tens = (num % 100) // 10
    units = num % 10

    out = str(num) + ' = '

    if hundreds > 0:
        out += str(hundreds) + ' centena'
        if hundreds > 1:
            out += 's'

        if tens > 0:
            if units > 0:
                out += ', '
            else:
                out += ' e '
        else:
            if units > 0:
                out += ' e '

    if tens > 0:
        out += str(tens) + ' dezena'
        if tens > 1:
            out += 's'

        if units > 0:
            out += ' e '

    if units > 0:
        out += str(units) + ' unidade'
        if units > 1:
            out += 's'

    print(out)