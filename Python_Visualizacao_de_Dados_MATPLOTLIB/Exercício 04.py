""" 04 - Dados: Percentual de vendas de diferentes produtos em uma loja.
produtos = ['Prod A', 'Prod B', 'Prod C', 'Prod D', 'Prod E']
vendas_percentual = [30, 25, 20, 15, 10]
Pergunta: Qual é a proporção de vendas de cada produto na loja?
Tarefa: Escolha entre gráfico de pizza e gráfico de barras para representar os dados.
Inclua título, rótulos dos eixos e legendas conforme apropriado.
Exercícios"""

import matplotlib.pyplot as plt
produtos = ['Prod A', 'Prod B', 'Prod C', 'Prod D', 'Prod E']
vendas_percentual = [30, 25, 20, 15, 10]
plt.pie(vendas_percentual, labels=produtos, autopct='%1.1f%%', explode=[0.05, 0.01, 0.01,0.01, 0.01], startangle=90)
plt.title("Vendas de cada produto")
plt.axis('equal')
plt.show()
