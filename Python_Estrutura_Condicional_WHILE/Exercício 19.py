# 19 - Fazer um programa que solicita um número inteiro positivo N ao usuário e imprime o seguinte padrão na tela.
# Por exemplo, para N = 5:

# +

# ++

# +++

# ++++

# +++++

loop = int(input("Digite a quantidade de repetições do operador + que você deseja imprimir: "))
print(f"Você digitou: {loop}")
print("FOR")
for contador in range(loop):
    print(f"{'+'* (contador+1)} \n")

print("WHILE")
contador = 0
while contador < loop:
    print(f"{'+' * (contador+1)} \n")
    contador +=1