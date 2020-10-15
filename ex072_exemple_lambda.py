def soma(x, y, z):
    return x + y + z


a = soma(1, 2, 3)
print(a)


f = (lambda x, y, z: x + y + z)
print(f(1, 2, 3))

d = (lambda x: lambda y: x + y)
e = d(3)
print(e(2))
