"""
08 - Transponha uma matriz.
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4], [5, 6]])`, o resultado seria `array([[1, 3, 5], [2, 4, 6]])
"""
import numpy as np
matriz = np.array([[1, 2], [3, 4], [5, 6]])
nova_matriz = matriz.T
print(nova_matriz)
