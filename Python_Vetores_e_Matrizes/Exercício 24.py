"""24 - Uma operação comum em ciência de dados ou aprendizado de máquina é a normalização dos dados. Os
dados estão dispostos em uma matriz e cada característica de interesse ao longo das colunas. Por exemplo,
uma matriz em que cada linha corresponde a uma pessoa, teremos a coluna das idades, a coluna das
alturas, a coluna da renda mensal, etc. A normalização consiste em, para cada ponto na matriz, subtrair a
média da coluna e dividir pelo desvio padrão da respectiva coluna.
Normalize os dados da seguinte matriz X, onde cada linha corresponde a uma amostra (e.g. pessoa) e cada
coluna corresponde a uma característica dela. Para normalizar os dados, você pode usar broadcasting para
subtrair a média de cada coluna e dividir pelo desvio padrão, evitando a necessidade de loops explícitos.
Dica: use os métodos mean(), std() para os cálculos da média e desvio padrão, respectivamente."""
import numpy as np
# Criando array
x = np.array([[55, 1.72, 603], [54, 1.42, 646], [44, 1.89, 964], [38, 1.79, 529]])
# Matriz X de forma transposta.
m = x.T

# Calculando a média das colunas transpostas.
medio = np.mean(m, axis=1)
# Calculando o desvio padrão das colunas transpostas.
desvio = np.std(m, axis=1)
# Subtração dos valores da matriz real com a média, com o resultado dividido pelo Desvio Padrão.
calculo = (x - medio) / desvio

# Imprimindo de forma abreviada para 3 casas decimais.
print(np.round(calculo, 3))
