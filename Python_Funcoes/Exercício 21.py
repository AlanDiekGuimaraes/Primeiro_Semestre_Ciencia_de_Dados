# 21 - Implemente uma função que dado um número n e retorna a menor potência de 2 maior ou igual a n.
# Por exemplo, pot2(14) retornará 16, pot2(42) retornará 64.

def pot2(n):
    potencia = 1
    while potencia < n:
        potencia *= 2
    return potencia
pot2(10)