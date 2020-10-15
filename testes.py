def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def fatorial_rec(n):
    if n == 1:
        return n
    return fatorial_rec(n - 1) * n


print(fatorial(5))
print(fatorial_rec(5))



