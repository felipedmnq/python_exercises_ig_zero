'''
Faça uma função que some impostos.

    A função possui dois parâmetros:
        - taxaImposto - % do imposto sobre vendas.
        - custo - valor do item sem imposto.

    Função inclui o imposto ao cisto.
'''


def sum_tax(tax, value):
    '''
    Calculates the product price with taxes.
    :param tax: tax rate (%)
    :param value: value product without taxes.
    :return: total price
    '''
    return (f'{value * (1 + (tax / 100)):.2f}')


print(sum_tax(15, 100))