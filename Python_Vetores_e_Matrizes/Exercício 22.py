"""22 - Calcule a média de cada coluna de uma matriz e as subtraia das respectivas colunas.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, o resultado seria
array([[-3., -3., -3.], [ 0., 0., 0.], [ 3., 3., 3.]])`. Use broadcasting para evitar loops"""
import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Matriz Transposta
m = matriz.T
# np.mean() responsável por calcular a média.
media = np.mean(m, axis=1)

# Imprimindo
print(matriz - media)
