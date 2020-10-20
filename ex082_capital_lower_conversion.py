'''
Faça duas funcões convertendo uma string entre maiusculo e minusculo.
'''
def main():
    string = 'ChiCleTe'

    print(all_tiny(string))
    print(all_capital(string))


def all_tiny(string):
    tiny = ''

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        tiny += char

    return tiny


def all_capital(string):
    capital = ''

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        capital += char

    return capital


main()