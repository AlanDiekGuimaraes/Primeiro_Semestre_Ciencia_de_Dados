# 07 - Função para retorno multiplo de valores.

def soma_pn(valores):
  soma_p = 0
  soma_n = 0
  for n in valores:
    if n > 0 :
      soma_p += n
    else:
      soma_n += n
  return soma_p, soma_n

valores = [2, -1, 3, -4]
soma_p, soma_n = soma_pn(valores)
print(f"""Soma dos positivos = {soma_p}
Soma dos negativos = {soma_n}""")