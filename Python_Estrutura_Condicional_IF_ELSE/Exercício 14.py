# 14. Faça um programa que receba a idade de uma pessoa e imprima sua condição
# (obrigatória, optativa ou proibida), em relação ao ato de votar, conforme apresentado abaixo:
#  Pessoas com idade menor que 16 anos são proibidas de votar (proibido);
#  Pessoas com idade igual a 16 e menor que 18 anos não são obrigadas a votar (optativo);
#  Pessoas com idade igual a 18 e menor que 65 anos são obrigadas a votar (obrigatório);
#  Pessoas com idade igual ou maior a 65 anos não são obrigadas a votar (optativo).

idade = int(input("Informe sua idade: "))

while idade <= 0 or idade >= 150:
  print("Idade Invalida")
  idade = int(input("Informe sua idade: "))

if idade < 16 :
  print("Proibido votar")
elif idade >= 16 and idade < 18 or idade >= 65:
  print("Voto optativo")
elif idade >= 18 and idade < 65:
  print("Voto obrigatória")