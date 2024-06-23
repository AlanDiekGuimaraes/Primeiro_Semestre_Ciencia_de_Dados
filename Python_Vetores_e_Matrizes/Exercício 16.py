"""16 - Determine uma constante que ao multiplicar todos os elementos de uma matriz por
essa constante, a soma dos elementos da matriz resultante será 1. Não usar loops.
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4]])`, o resultado seria `array([[0.1, 0.2], [0.3,
0.4]])`, pois 0.1+0.2+0.3+0.4 = 1."""
import numpy as np
matriz = np.array([[1, 2], [3, 4],[5, 6]])
soma = np.sum(matriz)
vetor = matriz * (1/soma)
print(vetor)
print(round(np.sum(vetor)))
