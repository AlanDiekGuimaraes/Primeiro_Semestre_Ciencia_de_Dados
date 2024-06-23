""" 03 - Dados: Salários de uma empresa por departamento.
DeptoA = [3000, 3200, 3500, 3800, 4000, 4200, 4500, 4800, 5000]
DeptoB = [2800, 2900, 3100, 3300, 3500, 3600, 3800, 4000, 4200]
DeptoC = [2500, 2700, 3000, 3200, 3300, 3500, 3700, 3900, 4100]
Pergunta: Qual é a distribuição dos salários por departamento?
Tarefa: Escolha entre box plot e histograma para representar os dados.
Inclua título, rótulos dos eixos e legendas conforme apropriado.
"""
import matplotlib.pyplot as plt
DeptoA = [3000, 3200, 3500, 3800, 4000, 4200, 4500, 4800, 5000]
DeptoB = [2800, 2900, 3100, 3300, 3500, 3600, 3800, 4000, 4200]
DeptoC = [2500, 2700, 3000, 3200, 3300, 3500, 3700, 3900, 4100]
plt.hist([DeptoA, DeptoB, DeptoC], edgecolor='black', alpha=1, bins=10)
plt.title("Distribuição dos salários por departamento")
plt.xlabel("Salários")
plt.ylabel("Distribuição")
plt.legend(["A", "B", "C"])
plt.grid(True)
plt.show()

