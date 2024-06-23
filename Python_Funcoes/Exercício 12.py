# 12 - Função taboada
def taboada(n):
    """
    Apresenta a taboada do inteiro n,
    onde 1 <= n <= 9.
    """
    print(f"Taboada do {n}".center(10))
    print(("-" * 12).center(10))
    contador = 0
    for contador in range(0,11):
        resultado = n * contador
        print(f"{contador:2d} X {n:1d} = {resultado:3d}")

taboada(10)