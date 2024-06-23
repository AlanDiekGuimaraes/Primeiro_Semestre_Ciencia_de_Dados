# 13. Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de
# Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta
# do usuário, faça a devida conversão.

escolha = int(input("Digite qual opção da corversão: 1 Fahrenheit → Celsius e 2 Celsius →  Fahrenheit "))
while escolha < 1 or escolha > 2:
  print("Valor inválido")
  escolha = int(input(f"Digite qual opção da corversão: 1 Fahrenheit → Celsius e 2 Celsius →  Fahrenheit "))

if escolha == 1:
  temperatura_f = float(input("Informe qual a temperatura Fahrenheit atual: "))
  temperatura = (temperatura_f - 32) * (5/9)
  print(f"temperatura em Celsius é: {temperatura:.2f} °C")
else:
  temperatura_c = float(input("Informe qual a temperatura Celsius atual: "))
  temperatura = (temperatura_c * (9/5)) + 32

  print(f"temperatura em Fahrenheit é: {temperatura:.2f} °F")