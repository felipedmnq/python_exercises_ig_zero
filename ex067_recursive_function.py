'''
função recursiva que imprima de um número x até um npumero y
'''

def x_y(x, y):
    print(x, end=' ')
    while x != y:
        print(x - 1, end=' ')
        x -= 1


def x_y_2(x, y):
    if x == y:
        return y
    return x_y(x - 1, y)


print(x_y_2(5, 1))



x_y(9, 1)