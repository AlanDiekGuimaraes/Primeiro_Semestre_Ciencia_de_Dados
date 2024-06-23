# 05 - Escreva um programa que troque o primeiro com o último elemento de uma lista qualquer.

lista = [12,95,33,66,80,25,17,28,77,60]
print([lista[-1]]+lista[1:-1]+[lista[0]])

print("Resultado 01 do professor")
lista[0], lista[-1] = lista[-1], lista[0]
print(lista)

print("Resultado 02 do professor")
primeiro = lista.pop(0)
ultimo = lista.pop()
lista.append(ultimo)
lista.insert(0, primeiro)
print(lista)