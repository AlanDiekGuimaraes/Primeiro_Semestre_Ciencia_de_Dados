# 15 - Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1 todos os números negativos.
# Realizar o exercício usando loops for e while. Exemplo para N igual a 5:
#Todos os resultados negativos

T = int(input("Entre com número inteiro maior que 1 para ver mais uma solução"))
#Outra solução
#FOR
print(f"For2:", end="")
for t in range(T): #Para o contador t dentro do range do numero apresentado faça
  print(f"{t-T}", end=" ") #Mostre o calculo de T-t
print("\n")
#WHILE
print(f"While2:", end=" ")
i = 0
while i < T: # Enquanto o contador for menor que o numero apresentado faça
  print(f"{i-T}", end=" ") #Mostre o calculo de T-t
  i += 1