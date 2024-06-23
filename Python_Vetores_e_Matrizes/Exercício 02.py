"""
02 - Implemente a função dot(v1, v2) que retorna o produto
escalar dos vetores v1 e v2. Cheque em sua implementação
que os vetores tenham o mesmo tamanho.
"""


def dot(v1, v2):
    if len(v1) != len(v2):
        print("Vetores com tamanhos diferentes")
        return
    soma = 0

    for n1, n2 in zip(v1, v2):
        soma = soma + n1 * n2
    return soma


Resposta = dot([1, 2, 3], [-1, 1, 1])
print(Resposta)


def dot2(v1, v2):
    return sum([n1*n2 for n1, n2 in zip(v1, v2)])


Resposta2 = dot2([1, 2, 3], [-1, 1, 1])
print(Resposta2)
