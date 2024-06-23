# 22 -  Implemente uma funçao que dado um número natural maior do que 1, decomponha esse número em fatores primos. Por exemplo, se o argumento de entrada for 36, a saída deverá ser [2, 2, 3, 3], porque 2 x 2 x 3 x 3 = 36.

def fatores_primos(numero):
    fatores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            fatores.append(divisor)
            numero /= divisor
        divisor += 1

    return fatores
fatores_primos(36)