# 19 - Implemente a função todos_diferentes(sequencia)que retorna True se todos os elementos de sequencia forem diferente, e retorne False caso contrário, isto é, pelo menos um elemento seja igual a outro componente da sequencia.

lista = [1,2,3,4,6]
def todos_diferentes(lista):
    tamanho_lista = set(lista)
    return len(tamanho_lista) == len(lista)

todos_diferentes(lista)