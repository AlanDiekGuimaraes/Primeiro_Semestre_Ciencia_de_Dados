# 32 - Função para resolver a equação de 2º grau.
def eqgrau2(a, b, c):
    """
    Resolve:
    a * X**2 + b * x + c = 0
    """
    delta = (b**2 -4 * a * c)
    if delta < 0:
        print(f"Delta ({delta}) é menor do que zero!")
        return None
    rdelta = raiz(delta)
    x1 = (-b - rdelta) / (2 * a)
    x2 = (-b + rdelta) / (2 * a)
    return x1, x2


a, b, c = 1, -5, 6
eqgrau2(a, b, c)
print(eqgrau2(a, b, c))


a, b, c = 10, 1, 1
eqgrau2(a, b, c)

