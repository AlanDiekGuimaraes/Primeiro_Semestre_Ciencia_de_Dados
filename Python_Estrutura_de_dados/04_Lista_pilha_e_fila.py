# -*- coding: utf-8 -*-
"""
Criar uma lista e posterioemete adicionar elementos

Usar conceitos de Pilha
Usar conceitos de Fila
"""

lista = []

def enfileirar(elemento):
    lista.append(elemento)
    print(f'O elemento {elemento} foi adicionado a lista')

def desenfileirar():
    if len(lista) > 0:
        primeiro_elemento = lista.pop(0)
        print(f"Elemento {primeiro_elemento} foi desenfileirado")
    else: 
        print("A fila esta vazia")
        
def empilhar(elemento):
    lista.append(elemento)
    print(f'O elemento {elemento} foi empilhado')

def desempilhar():
    if len(lista) > 0:
        topo = lista.pop()
        print(f'Elemento {topo} foi desempilhado')
    else:
        print('A pilha está vazia')

enfileirar('Lasanha')

