# nonlocal
# lista de supermercado.


def lista_mercado():
    start = 0
    lista = []
    def increment(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(start, '-\t', item)
    return increment


compras1 = lista_mercado()

compras1('presunto')
compras1('pao')
compras1('queijo')
compras1('cerveja')
