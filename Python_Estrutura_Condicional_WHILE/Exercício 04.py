# 4. Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que: Esse funcionário foi contratado em 1995,
# com salário inicial de R$ 1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse
# funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

ano_inicio = 1995

salario = float(input("Digite o valor do salário inicial R$ "))
ano_final = float(input("Digite o ano atual R$ "))
percentual = 0.015
while ano_inicio < ano_final:
  aumento = salario * percentual
  salario += aumento
  percentual *=2
  ano_inicio += 1
print(f"O salario em {ano_final} é R$ {salario:.2f}")