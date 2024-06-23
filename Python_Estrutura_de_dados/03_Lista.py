# -*- coding: utf-8 -*-
"""
Lista:
    
"""

lista_frutas = ['Laranja', 'Maça', 'Pera', 'Banana', 'Kiwi']
print(lista_frutas)

primeira_fruta = lista_frutas[0]
print(primeira_fruta)

ultima_fruta = lista_frutas[-1]
print(ultima_fruta)

lista_frutas.append('Abacaxi')
print(lista_frutas)

lista_frutas.remove('Maça')
print(lista_frutas)

if 'Banana' in lista_frutas: 
    print('Tem Banana aqui dentro')

print(lista_frutas)

tamanho_da_lista = len(lista_frutas)
print(tamanho_da_lista)

for fruta in lista_frutas:
    print(f'Fruta: {fruta}')
    
frutas_em_maiusculo = [f.upper() for f in lista_frutas]
print(frutas_em_maiusculo)