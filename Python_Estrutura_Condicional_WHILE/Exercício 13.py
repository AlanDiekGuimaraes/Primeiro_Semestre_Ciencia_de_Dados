# 13 - Solicitar um numero inteiro positivo N ao usuario. imprimir os numeos de N a 1. Realizar o exercicio usando loops for e while
#variavel que será utilizada pelos 2 loops

n_numero = int(input("Entre com número inteiro maior que 1: "))

#FOR
print(f"For: ", end="")
for contador in range(n_numero):
  print(f"{n_numero-contador}", end=" ")
print("\n")
#WHILE
print(f"While: ", end="")
contador2 = 0
while contador2 < n_numero:
  print(f"{n_numero-contador2}", end=" ")
  contador2 += 1