'''
Retorne a soma de N até 0.
'''

def somaN(n):
    if n == 0:
        return n
    return (somaN(n - 1) + n)


print(somaN(6))