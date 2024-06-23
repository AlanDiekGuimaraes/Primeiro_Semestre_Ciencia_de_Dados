# 33 - Função para somar todos os numeros do intervalo de um enésimo  termo.

def soma_recursiva(n):
    if n == 1:
        return 1
    if n <=0:
        return 0
    return n + soma_recursiva(n-1)


print(soma_recursiva(100))

def soma_interativo(i):
    soma = 0
    for n in range(1, i + 1):
        soma += n
    return soma


print(soma_interativo(100))