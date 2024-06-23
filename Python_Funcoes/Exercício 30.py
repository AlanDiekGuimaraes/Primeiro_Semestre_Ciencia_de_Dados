# 30 - Função para Calcular raiz quadrada

def raiz(N):
    """Calcula a raiz quadrada de N
    Usando o algoritmo:
    x_(n+1) = 1/2 * (x_n + N/x_n)
     """
    if N == 0 or N == 1:
        return N
    if N < 0:
        N = -N
    x, n = 1, 0
    while abs(x*x - N)> 1e-9: # 0.00001 == 1e-5
        n += 1
        x = 1/2 * (x + N/x)
    return x

raiz(125)