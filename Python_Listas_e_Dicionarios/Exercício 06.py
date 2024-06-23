# 06 - Qual a saída/resultado da seguinte compreensão de lista?
# Você consegue entender e explicar o resultado?

m = [[1+j*3 + i for i in range(3)] for j in range(3)]
print(m)

lista = []
for j in range(3):
  lista.append([])
  for i in range(3):
    lista[j].append(1+j*3 + i)

print(lista)

# RESPOSTA  06

# No problema 06 da atividade de programação tem uma estrutura com 2 for, onde:
# No range i é feita a multiplicação e soma a cada passada no loop, neste caso o i fica responsável por adicionar os elementos na matriz, aumentando o i, aumenta a quantidade de itens da matriz.
# No range j é criada as matrizes em si, se aumentar o range do j aumenta a quantidade de matrizes.