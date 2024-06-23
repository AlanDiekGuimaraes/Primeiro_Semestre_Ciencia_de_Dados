# 2. Faça um programa que recebendo um valor inteiro, informe se o número é positivo,negativo ou neutro.

valor = int(input("Insira o valor: ")) # Solicita ao usuário o valor

if valor > 0: #Verifica sé o valor é maior do que 0 e informa que é positivo
  print("O valor é POSITIVO")
elif valor < 0: #Verifica sé o valor é menor do que 0 e informa que é negativo
  print("O valor é NEGATIVO")
else: # Caso não seja nenhuma das opções anteriores infoma que o valor é neutro
  print("Seu valor é NEUTRO")