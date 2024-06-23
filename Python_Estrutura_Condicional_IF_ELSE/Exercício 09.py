# 9. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input("Informe em qual turno você estuda. M para matutino, , V para Vespertino ou N para Noturno " )).upper()

while (turno != "M" and turno != "V" and turno != "N"):
  print("Desculpe, opção invalida")
  turno = str(input("Informe em qual turno você estuda. M para matutino, , V para Vespertino ou N para Noturno " )).upper()

if turno == "M":
  print("Bom dia")
elif turno == "V":
  print("Boa Tarde")
else:
  print("Boa Noite")