"""
14 - Reshape um vetor unidimensional em uma matriz 3x3. Exemplo: Seja `vetor =
np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])`, o resultado seria `array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
import numpy as np
vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
matriz = vetor.reshape(3, 3)
print(matriz)
