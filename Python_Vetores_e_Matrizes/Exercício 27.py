"""27 - Suponha que você seja um corretor imobiliário e deseja prever o preço de uma casa com base em diferentes
características, como área construída, número de quartos, número de banheiros e idade da casa. Você coletou
dados de venda de casas nos últimos seis meses e registrou essas características para cada venda.
Os dados coletados estão disponíveis na forma de uma matriz, onde cada linha representa uma casa vendida e
cada coluna representa uma característica. Além disso, você tem um vetor com os preços de venda
correspondentes das casas.
Tarefa:
Encontrar os coeficientes ideais que relacionam as características das casas com
os preços de venda. Em seguida, preveja o preço de uma nova casa com as
 seguintes características:
• Área construída: 180 metros quadrados
• Número de quartos: 3
• Número de banheiros: 2
• Idade da casa: 10 anos
(Resposta: 355000)"""


import numpy as np
# Criando primeira array
A = np.array([[150, 3, 2, 5],
              [200, 4, 3, 7],
              [180, 3, 2, 10],
              [170, 2, 1, 3],
              [220, 4, 3, 8],
              [190, 3, 2, 6]])

# Criando segunda array
B = np.array([[300000], [400000], [350000], [250000], [420000], [380000]])

# Fórmula usando biblioteca linalg
X, resultantes, _, _= np.linalg.lstsq(A, B, rcond=None)

# Nova casa
exercicio = np.array([[180, 3, 2, 10]])
# Imprmindo e realizando o dot() da nova matriz em relação com as variáveis.
print(exercicio @ X)