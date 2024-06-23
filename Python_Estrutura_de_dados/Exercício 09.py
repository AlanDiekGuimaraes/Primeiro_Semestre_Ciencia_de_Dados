"""
Para os próximos 3 exercícios, utilize os dados em `dados_ex1.pkl`, que contém Series
da quantidade de vendas diárias de um produto. Você pode ler esses dados da seguinte
forma:

vendas_diarias = pd.read_pickle('dados_ex1.pkl')

Exercício 1: Apresente:
a) O dia com o maior número de vendas e o valor correspondente
b) O dia com o menor número de vendas e o valor correspondente
c) O valor médio do número de vendas diárias no ano
d) O gráfico da quantidade de vendas diárias
"""

import pandas as pd

vendas_diarias = pd.read_pickle("dados_ex1.pkl")
print(f"""Dia com maior número de vendas: {vendas_diarias.idxmax()}, valor correspondente: {vendas_diarias.max()}""" )
print()
print(f"Dia com menos número de vendas: {vendas_diarias.idxmin()}, valor correspondente: {vendas_diarias.min()}")
print()
print(f"Valor médio das Vendas: {vendas_diarias.mean():.2f}")
vendas_diarias.plot(grid=True)
