def mode_receive():
    while True:

        mode = input('C - Criptografar.'
                     '\nD - Decriptografar.'
                     '\n'
                     '\nQual comando deseja executar?: ').upper().strip()

        if mode not in 'CD':
            print('ENTRADA INVÁLIDA!')
        if mode in 'CD':
            break

    return mode


def key_receive():
    while True:
        key = int(input('Digite o valor da chave [2 - 20]: '))

        if 2 <= key <= 20:
            break
        else:
            print('ENTRADA INVÁLIDA!')

    return key


def de_en_crypts(mode, msg, key):

    if mode == 'D':
        key *= -1
    decryptated = ''

    for simb in msg:
        if simb.isalpha():
            num = ord(simb)
            num += key

            if simb.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif simb.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

                decryptated += chr(num)

        else:
            decryptated += simb

    return decryptated


def main():
    mode = mode_receive()
    msg = input('Digite sua mensagem: ')
    key = key_receive()

    print(f'Seu texto traduzido é: {de_en_crypts(mode, msg, key)}.')


main()