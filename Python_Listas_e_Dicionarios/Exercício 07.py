# 07 - Considere que você recebe um dicionário contendo informações sobre produtos em uma loja.
# Cada chave do dicionário é o nome de um produto e cada valor é uma tupla contendo o preço
# e a quantidade em estoque desse produto.
# produtos = {
# 'camiseta': (25.00, 10),
# 'calça': (45.00, 5),
# 'sapato': (60.00, 3),
# 'boné': (15.00, 8) }
# Você deve criar um programa em Python que solicite ao usuário que insira um preço máximo.
# Em seguida, o programa deve imprimir os produtos cujo preço seja menor ou igual ao preço
# máximo inserido pelo usuário.

produtos = {'camiseta': (25.00, 10), 'calça': (45.00, 5), 'sapato': (60.00, 3), 'boné': (15.00, 8)}

menor_valor = []

preco = float(input("Digite o valor maximo que deseja que filtremos os produtos: "))

for chave, valor in produtos.items():
  if valor[0] <= preco :
    menor_valor.append(chave)

print(menor_valor)


preco_max =