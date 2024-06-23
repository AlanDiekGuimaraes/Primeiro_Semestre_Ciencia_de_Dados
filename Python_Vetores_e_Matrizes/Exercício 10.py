"""
10 - Multiplicação matricial: multiplique uma matriz (𝑚 × 𝑛) por um vetor (𝑛 × 1).
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4]])` e `vetor = np.array([[5], [6]]),
o resultado seria `array([[17], [39]])
"""
import numpy as np
matriz = np.array([[1, 2], [3, 4]])
vetor = np.array([[5], [6]])
print(matriz.dot(vetor))
