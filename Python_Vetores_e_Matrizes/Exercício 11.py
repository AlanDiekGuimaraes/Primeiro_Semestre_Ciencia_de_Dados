"""
11 - Encontre os índices dos valores máximos em cada linha de uma matriz.
Dica: use np.argmax(). Exemplo: Seja `matriz = np.array([[1, 9, 6], [8, 2, 3], [4, 7, 5]])`,
o resultado seria `array([1, 0, 1])
"""
import numpy as np
matriz = np.array([[1, 9, 6], [8, 2, 3], [4, 7, 5]])
arr = np.argmax(matriz, axis=1)
print(arr)
