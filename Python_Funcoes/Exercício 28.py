# 28 - Funcão interativa da função anterior
# Potencia (a,b) = a * a * a ..., b vezes


def potencia_interativa(base, expoente):
    pot = 1
    for contador in range(expoente):
        pot = pot * base
    return pot

potencia_interativa(6,3)