# 12. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input("Informe o dia da semana (1-Domingo, 2- Segunda, ...) "))

while dia_semana < 1 or dia_semana > 7:
  print("Valor Inválido")
  dia_semana = int(input("Informe o dia da semana (1-Domingo, 2- Segunda, ...) "))
if dia_semana == 1:
  print("Hoje é DOMINGO")
elif dia_semana == 2:
  print("Hoje é SEGUNDA-FEIRA")
elif dia_semana == 3:
  print("Hoje é TERÇA-FEIRA")
elif dia_semana == 4:
  print("Hoje é QUARTA-FEIRA")
elif dia_semana == 5:
  print("Hoje é QUINTA-FEIRA")
elif dia_semana == 6:
  print("Hoje é SEXTA-FEIRA")
elif dia_semana == 7:
  print("Hoje é SÁBADO")
#else:
 # print("Valor Invalido")