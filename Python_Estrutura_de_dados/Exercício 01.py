""" Implementação simples de pilha"""

def criar_pilha(capacidade):
    return [], capacidade

def is_empty(pilha):
    return len(pilha) == 0

def is_full(pilha):
    global capacidade
    return len(pilha) == capacidade

def push(pilha, elemento):
    if not is_full(pilha):
        pilha.append(elemento)
    else:
        print("Erro: Pilha cheia")

def pop(pilha):
    if not is_empty(pilha):
        return pilha.pop()
    else:
        print("Erro:Pilha vazia")
        
def peek(pilha):
    if not is_empty:
        return pilha(-1)
    else:
        print("Erro: Pilha vazia")
        return None

def verifica_balanceamento(expr):
   # capacidade = 100
    pilha = []
    for c in expr:
        if c == "(":
            pilha.append(c)
        elif c ==")":
            if len(pilha) == 0 or pilha.pop() != "(":
                return False
    return len(pilha) == 0

print(verifica_balanceamento("(1+(9))))"))
