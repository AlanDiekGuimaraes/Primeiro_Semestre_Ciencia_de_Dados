# 02 - Função para alternar sinal.

def alterna(N):
  mult = -1
  fat = -1
  for n in range(N+1):
    num = fat * n
    fat *= mult
    print(num, end=' ')
  print()

alterna(5)
alterna(9)
alterna(12)

