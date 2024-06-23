# 04 - Inicialize uma lista de 10 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.

lista = [12,95,33,66,80,25,17,28,77,60]
par = [contador for contador in lista if contador % 2 == 0]
impar = [contador for contador in lista if contador % 2 == 1]

print(f"""PARES: {par}
IMPARES:{impar} """)