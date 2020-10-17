'''
Are given two int numbers P and Q, being that the number of "P" digits is lower or equal of the numbers
of "Q" digits.

Check if "P" is a subnumber of "Q".
'''


def count_dig(num):
    '''
    It receives an INT number and returns the number of digits NUM.
    '''
    count = 0
    while num != 0:
        num //= 10
        count += 1

    return count


def main():
    p = int(input('P: '))
    q = int(input('Q: '))

    count_d = count_dig(p)
    aux_q = q

    while True:
        subnum = aux_q % (10 ** count_d)
        if subnum == p:
            break

        aux_q //= 10

        if aux_q == 0:
            break

    if subnum == p:
        print(f'{p} is sunumber of {q}.')
    else:
        print(f'{p} isnt subnumber of {q}.')


main()
