# 18 - Implemente a função todos_iguais(sequencia)que retorna True se todos os elementos de sequencia forem iguais, e retorne False caso contrário.

lista = [1,1,1,1]
def todos_iguais(lista):
    n = lista[0]
    for elemento in lista:
        if elemento != n:
            return False
    return True

todos_iguais(lista)