# 34 - Função para calcular a sequencia de fibonacci de um enésimo  termo.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))

[fibonacci(n) for n in range(1, 11)]