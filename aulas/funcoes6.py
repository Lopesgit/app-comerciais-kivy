# coding: utf-8

# Retorno de valores multiplos


def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo


q, c = potencia(10)

print(q)
print(c)

