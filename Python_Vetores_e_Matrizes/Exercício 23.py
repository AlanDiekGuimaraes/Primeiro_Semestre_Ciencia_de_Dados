"""23 - Calcule a média de cada linha de uma matriz e as subtraia das respectivas linhas.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, o resultado seria
array([[-1., 0., 1.], [-1., 0., 1.], [-1., 0., 1.]])`. Use broadcasting para evitar loops"""
import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# np.mean() responsável por calcular a média. [2, 5, 8]
media = np.mean(matriz, axis=1)
# Criando arrays para cada média que nela compõe. [[2][5][8]]
update = media.reshape(3, 1)
# Imprimindo
print(matriz - update)
