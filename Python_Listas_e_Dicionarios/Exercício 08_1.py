# 08 - Em uma competição de ginástica, cada atleta recebe votos de
# sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica
# sendo a média dos votos restantes. Você deve fazer um programa
# que receba o nome do ginasta e as notas dos sete jurados
# alcançadas pelo atleta em sua apresentação e depois informe a sua
# média, conforme a descrição acima informada (retirar o melhor e o
# pior salto e depois calcular a média com as notas restantes). As
# notas não são informadas em ordem crescente ou decrescente.

#minha solução
nome = input("Insira o nome do atleta: ").title()
notas = [] # Cria uma lista vazia

for contador in range(1,8): # faz o loop.
  nota = float(input(f"Insira a {contador}ª nota do salto: ")) # Recebe as notas do atleta.
  notas.append(nota) # Adiciona a nota na lista NOTAS
notas.sort()  #Classifica em ordem crecente a lista
notas.pop(0)  # .pop(0) remove o primeiro elemento da lista
notas.pop()   # .pop() remove o ultimo elemento da lista

# notas.remove(max(notas)) # Remove o valor Máximo da lista NOTAS
# notas.remove(min(notas)) # Remove o valor Minimo da lista NOTAS

media = sum(notas)/len(notas) # soma as notas e calcula a média.

print(f"O atleta {nome} teve uma média de {media:.2f} pontos.")