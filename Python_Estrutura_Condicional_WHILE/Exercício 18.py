# 18 - Fazer um programa que solicita um número inteiro positivo N ao usuário e imprime o seguinte padrão na tela.
# Por Exemplo, para

# N = 5
#  -----
# |     |
# |     |
# |     |
# |     |
# |     |
#  -----

sinal = "-"
espaco = " "
while True:
  repeticoes = int(input("Insira a quantidade de repetições: "))
  print(f" {sinal*repeticoes}")
  for i in range(repeticoes):
    print(f"|{espaco*repeticoes}|")
  print(f" {sinal*repeticoes}")
  break