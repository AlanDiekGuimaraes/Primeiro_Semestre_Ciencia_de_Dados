# 27 - Função recursiva potencia (a,b)
# potencia(a,b) = a * potencia(a,b-1)
# caso base: potencia(a, 0) = 1


def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente-1)

potencia(5,3)