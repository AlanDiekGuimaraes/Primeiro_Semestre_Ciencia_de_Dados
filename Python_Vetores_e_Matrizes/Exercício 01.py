"""
01 - Crie uma função, mult(v, N), que recebe um vetor v e um
número N e retorna cada elemento do vetor multiplicado por esse número.
"""


def mult(v, n):

    """
    Multiplica o vetor v pela constante N.
    """
    return [n * elemento for elemento in v]


v = [1, 2, 3, 3]
w = mult(v, 5)
print(w)
