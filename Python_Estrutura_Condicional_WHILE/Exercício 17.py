# 17 - Solicitar uma palavra ao usuário e dizer se a palavra é um palindromo, isto é,
# pode ser lida igualmente da esquerda para a direita e vice-versa. Exemplos de palavras que são palíndromos:
# Ovo, radar, mirim, arara reviver.

palavra = input("Digite a palavra: ").upper().strip()
inverso = ""
for contador in range(len(palavra)-1,-1,-1):
    inverso += palavra[contador]
if palavra == inverso:
    print(f"""A palavra é polidromos:
Digitado {palavra}
Inverso {inverso}
  """)
else:
    print(f"""A palavra não é polidromos:
Digitado: {palavra}
Inverso: {inverso}""")