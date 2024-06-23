# 08- Implemente a função somas(lista) que recebe uma lista de números e retorna a soma dos números e a soma dos números ao quadrado.

def somas(lista):
  soma1, soma2 = 0, 0
  for num in lista:
    soma1 = soma1 + num
    soma2 = soma2 + num * num
  return soma1, soma2

lista = [1, 2, 3, 4, 5, -1, 2.2, 3.1415]

soma1, soma2 = somas(lista)
print(f"""Soma = {soma1:.2f}
Soma ao quadrado = {soma2:.2f}""")
