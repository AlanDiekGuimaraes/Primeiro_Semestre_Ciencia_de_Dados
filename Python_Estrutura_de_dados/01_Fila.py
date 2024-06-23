
"""
Fila:
    FIFO
    Primeiro a entrar é o primeiro a sair
    
"""

fila = []

def enfileirar(elemento):
    fila.append(elemento)
    print(f"Elemento {elemento} foi enfileirado")
    
def desenfileirar():
    if len(fila) > 0:
        primeiro_elemento = fila.pop(0)
        print(f"Elemento {primeiro_elemento} foi desenfileirado")
    else:
        print("A fila esta vazia")
        
    
enfileirar(3)
enfileirar(5)
enfileirar(9)
enfileirar(3)
enfileirar(5)
enfileirar(9)

print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

desenfileirar()
desenfileirar()
desenfileirar()

print(fila)
print(len(fila))

desenfileirar()
