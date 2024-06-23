# 1. Leia dois números, faça a soma e apresente caso seja maior que 15.

nota1 = float(input("Insira o primeiro número: ")) # Solicita o primeiro número ao usuário

nota2 = float(input("Insira o segundo número: ")) # Solicita o segundo número ao usuário

soma = nota1 + nota2 # Calcula a soma

if soma > 15: #verifica se a soma é maior que 15
  print(f"A soma dos valores é {soma:.2f}") # printa na tela se o valor for maior que 15, senão finaliza o programa.
else:
  print("O valor informado está abaixo do esperado")