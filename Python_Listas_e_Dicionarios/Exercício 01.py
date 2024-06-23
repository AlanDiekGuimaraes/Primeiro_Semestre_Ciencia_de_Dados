# 01 - Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sia posição na lista.
print("Lista 01: ")
lista1 = [-7, 2, 20, -4, 5]
contador = 0
while contador < len(lista1):
    print(f"{contador}:{lista1[contador]}")
    contador += 1

print("Lista 02: ")
lista2 = [-7, 2, 20, -4, 5]
contador = 1
for item in lista2:
    print(f"{contador}:{item}")
    contador += 1

print("Lista 03: ")

lista3 = [-7, 2, 20, -4, 5]
contador = 1
for item in lista3:
    print(f"{contador}:{item}")
    contador += 1
print("Lista 04: ")
lista4 = [-7, 2, 20, -4, 5]
for idx, item in enumerate(lista4):
    print(f"{idx}:{item}")