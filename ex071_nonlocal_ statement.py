'''
Reescreva o exercício 64 - coloque todas as fuções dentro de main e utilize "nonlocal" statement.
'''



def main():
    counts = []
    deposits = []
    balance = 0


    def create_acount():
        nonlocal counts, deposits, balance
        num_count = int(input('Número da conta: '))

        while num_count in counts:
            print(f'Conta já existente. Digite novamente.')
            num_count = int(input('Número da conta: '))

        counts.append(num_count)

        deposit = float(input('Valor do depósito: R$ '))
        while deposit <= 0:
            print('Valor inválido.')
            deposit = float(input('Valor do depósito: R$ '))

        deposits.append(deposit)
        balance += deposit

    def see_balance():
        option = bool(int(input('Deseja visualizar o saldo?\n1 - Sim \n0 - Não\n\nOpção: ')))
        if option:
            print(f'O saldo é: R$ {balance}.')

    option = bool(int(input('Deseja criar uma nova conta?\n1 - SIM.\n2 - NÃO - "Fechar programa".\nOpção: ')))
    while option:
        create_acount()
        see_balance()
        option = bool(int(input('Deseja criar uma nova conta?\n1 - SIM.\n2 - NÃO - "Fechar programa".\nOpção: ')))


main()