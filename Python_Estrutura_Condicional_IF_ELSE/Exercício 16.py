# 16. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Informe o valor do primeiro produto R$"))
preco2 = float(input("Informe o valor do segundo produto R$"))
preco3 = float(input("Informe o valor do terceiro produto R$"))

menor = preco1

if menor > preco2:
  menor = preco2
  if menor > preco3:
    menor = preco3
elif menor > preco3:
  menor = preco3
print(f"O menor preco é R${menor}")