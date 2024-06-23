# 35 - Função para calcular o PI.

def estima_pi(n):
    return 4 * sum([1 / ((2 * x + 1) * (-1) ** x) for x in range(n)])


print(estima_pi(100000))
