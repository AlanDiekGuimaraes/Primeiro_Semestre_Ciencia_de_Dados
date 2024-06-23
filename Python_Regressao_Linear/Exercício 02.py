"""Exercício de Regressão Linear Simples
Estudo do Desempenho de um Motor de Combustão Interna
Você foi contratado como analista de dados por uma empresa automotiva líder para estudar o desempenho de um novo
motor de combustão interna. O objetivo é entender como a quantidade de combustível injetado afeta a temperatura do
motor durante o funcionamento.
Você recebeu um conjunto de dados que contém informações sobre a quantidade de combustível injetado por minuto
(em litros por minuto) e a temperatura do motor correspondente (em graus Celsius). Sua tarefa é analisar esses dados e
construir um modelo de regressão linear para prever a temperatura do motor com base na quantidade de combustível
injetado.
- Quantidade de Combustível Injetado x: de 0 a 10 litros por minuto (l/min).
- Temperatura do Motor y: de 15°C a 150°C.

Exercício de Regressão Linear Simples
Instruções:
1. Carregue os dados do arquivo combustivel_e_temperatura.npy fornecido.
2. Visualize os dados usando um gráfico de dispersão para entender a relação entre a quantidade de combustível
injetado e a temperatura do motor.
3. Estime um modelo de regressão linear simples usando os dados.
4. Calcule o coeficiente de determinação (R2) para avaliar o ajuste do modelo.
5. Faça uma previsão da temperatura do motor para uma quantidade de combustível injetado de 8 litros por minuto
usando o modelo. (Resposta: 121.5°C)
Entrega:
- Apresente o código Python usado para carregar os dados, visualizar os dados, estimar o modelo, calcular R2 e fazer a
previsão.
- Inclua comentários explicativos em seu código para facilitar a compreensão.
- Apresente suas conclusões e interpretações com base nos resultados obtidos.
"""

import numpy as np  # Importa a Biblioteca Numpy
import matplotlib.pyplot as plt  # Importa a Biblioteca MatploitLib
# dados
dados = np.load("combustivel_e_temperatura.npy")  # Ler o arquivo da pasta local
x, temperatura = dados

# Solução np.lstsq()
litros = np.vstack((np.ones(len(x)), x)).T
betas, res, _, _ = np.linalg.lstsq(litros, temperatura, rcond=None)
beta0, beta1 = betas
residuo = res[0]


# Calculando a previsão do modelo
y_prev = beta1 * x + beta0

# Calcula o R-quadrado
y_medio = np.mean(temperatura)
tss = np.sum((temperatura - y_medio) ** 2)  # Soma o total dos quadrados
rss = np.sum((temperatura - y_prev) ** 2)  # Resíduo dos quadrados
r2 = 1 - rss / tss

plt.scatter(x, temperatura, label="Reais")  # Cria pontinhos no grafico.
# plt.scatter(x, y_prev, label="Estimados")

plt.xlabel("Litros consumidos")  # Cria o label na coordenada x.
plt.ylabel("Temperatura do Motor")  # Cria o label na coordenada y.
plt.plot(x, beta0 + beta1 * x, "r--", alpha=0.2, label="Modelo")  # Plota a linha no grafico.
plt.legend()  # Cria a legenda
plt.show()  # Exibe o gráfico.

print(f"Intercepto, {beta0=:.5f} ")
print(f"Coeficiente angular, {beta1=:.5f} ")
print(f"R-quadrado, {r2=:.5f}")
print(f"Residuo de lstsq(): {residuo=:.5f}")
print(f"Residuo calculado: {rss=:.5f}")

