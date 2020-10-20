'''
Faça um programa que peça o nome e a senha de usuário e não aceite uma senha igual ao nome do usuário.
'''
def main():
    #name   = input('Nome do usuário: ').upper()
    #passwd = input('Senha do usuário: ').upper()
    name   = input('Nome do usuário: ')
    passwd = input('Senha do usuário: ')

    while all_capital(name) == all_capital(passwd):
        print('Senha inválida. A senha não pode ser igual ao nome do usuário.')
        passwd = input('Senha do usuário: ')


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