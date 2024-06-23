# 01 - Função para receber nome e idade.

def saudacao(nome, idade):
  print("Olá,",nome,"sua idade é", idade,"anos.")
def linha_cabecalho():
  print("-" * 50)



nome = input("Entre com seu nome: ").title()
idade = int(input("Digite sua idade: "))

linha_cabecalho()
saudacao(nome, idade)
linha_cabecalho()

