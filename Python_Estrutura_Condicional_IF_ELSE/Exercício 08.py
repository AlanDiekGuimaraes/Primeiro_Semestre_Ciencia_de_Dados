# 8. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time)
# e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

placar1 = int(input("Informe qual foi o placar da seleção BRASILEIRA "))

placar2 = int(input("Informe qual foi o placar da seleção ARGENTINA "))

if placar1 > placar2:
  print("a Selecão BRASILEIRA foi campeã ")
elif placar2 > placar1:
  print("a Selecão ARGENTINA foi campeã ")
else:
  print("O resultado do jogo foi empate ")