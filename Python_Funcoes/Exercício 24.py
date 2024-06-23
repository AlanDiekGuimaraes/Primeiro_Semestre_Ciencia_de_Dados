# 24 - Implemente uma função recursiva div(m, n) que recebe como argumentos dois números naturais m e n e devolve o resultado da divisão inteira de m por n . Não pode recorrer às operações aritméticas de multiplicação, divisão inteira e resto da divisão inteira.
# Digite o valor de m (dividendo): 7
# Digite o valor de n (divisor): 2
# A divisão inteira de 7 por 2 é: 3


def div(m, n):
    if m < n:
        return 0
    return 1 + div(m - n, n)

m = int(input("Digite o valor de m (dividendo): "))
n = int(input("Digite o valor de n (divisor): "))
print(f"A divisão inteira de {m} por {n} é: {div(m,n)}")