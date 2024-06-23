"""
09 - Converta uma matriz em um vetor unidimensional.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6]])`, o resultado seria `array([1, 2, 3, 4, 5, 6])
"""
import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6]])
matriz1 = matriz.reshape(-1)
print(matriz1)
