# 23 - Implemente a função maiorN(lista, N) que recebe uma lista de números quaisquer, um valor N, 1 <= N <= len(lista), e retorna o Nésimo maior valor na lista de números. Por exemplo, se N for 1, retorna o maior valor na lista, se N for 2, retorna o segundo maior valor na lista, etc. Exemplo:
# lista = [5, -1, 7, 0, -3, 9]
# N = 2
# print{f'Em {lista} o {N}o. maior valor é {maiorN{lista, N)}')
# Em [5, -1, 7, 0, -3, 9] o 2o. maior valor é 7


lista = [1, 2, 3, 4, 5]
n = -1


def maior(n, lista):
    lista.sort()
    return lista[n]


maior(n, lista)
