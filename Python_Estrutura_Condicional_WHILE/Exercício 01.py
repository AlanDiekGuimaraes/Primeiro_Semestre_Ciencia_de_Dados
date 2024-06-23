# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um Valor válido.

nota = int(input("Digite o valor da nota entre 0 e 10: "))
while nota < 0 or nota > 10:
  print("Nota invalida")
  nota = int(input("Digite o valor da nota entre 0 e 10: "))
  print(f"A nota digitada foi: {nota}")