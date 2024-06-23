""" 01 - Dados: Alturas (em centímetros) de uma amostra de estudantes de uma escola.

np.random.seed(2)
alturas = np.random.normal(170, 3, 300)

Pergunta: Qual é a distribuição das alturas dos estudantes?

Tarefa: Escolha entre histograma e gráfico de barras para representar os dados. Inclua
título, rótulos dos eixos e legendas conforme apropriado."""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
alturas = np.random.normal(170, 3, 300)
plt.hist(alturas, bins=20, edgecolor='black')
"""plt.plot(alturas)"""
plt.title("Alturas dos estudantes")
plt.xlabel("Altura")
plt.ylabel("Distribuição")
plt.grid(True)
plt.show()
