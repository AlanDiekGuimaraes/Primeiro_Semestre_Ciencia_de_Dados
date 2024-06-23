# 20 - Implemente uma função que recebe como argumentos um número n e uma lista de números, indice_elemento(n, lista).
# A função retornará o índice da primeira ocorrência do número na lista e -1 se o número não estiver na lista. OBS: em python, índices de listas, arrays, etc.começam em 0.

lista = [10, 20, 30, 40, 50]

def indice_elemento(n, lista):
    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1

n = 55
indice_elemento(n, lista)

