# -*- coding: utf-8 -*-
"""
Pilha:
    LIFO
    Ultimo a entrar é o primeiro a sair
"""

pilha = []

def empilhar(elemento):
    pilha.append(elemento)
    print(f'O elemento {elemento} foi empilhado')

def desempilhar():
    if len(pilha) > 0:
        topo = pilha.pop()
        print(f'Elemento {topo} foi desempilhado')
    else:
        print('A pilha está vazia')
        

empilhar(3)
empilhar(5)
empilhar(9)
print(pilha)
print(len(pilha))

desempilhar()
print(pilha)
print(len(pilha))

desempilhar()
print(pilha)
print(len(pilha))

desempilhar()
print(pilha)
print(len(pilha))

desempilhar()