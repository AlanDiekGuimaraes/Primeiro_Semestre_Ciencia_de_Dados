""" 02 - Dados: Notas em matemática e em ciências de uma turma ao longo do tempo.
Tempo: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Notas de Ciências: [80, 85, 70, 90, 75, 85, 95, 80, 85, 90]
Notas de Matemática: [70, 75, 65, 85, 60, 80, 90, 75, 80, 85]
Pergunta: Existe alguma relação entre as notas em matemática e em ciências ao longo do
tempo?
Tarefa: Escolha entre scatter plot e gráfico de linhas para representar os dados. Inclua
título, rótulos dos eixos e legendas conforme apropriado."""

import matplotlib.pyplot as plt
tempo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas_ciencias = [80, 85, 70, 90, 75, 85, 95, 80, 85, 90]
notas_matematica = [70, 75, 65, 85, 60, 80, 90, 75, 80, 85]
plt.plot(tempo, notas_ciencias, color="red", marker="o")
plt.plot(tempo, notas_matematica, color="blue", marker="o")
plt.title("Notas ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("Notas")
plt.grid(True)
plt.legend(["Ciências", "Matemática"])
plt.show()
