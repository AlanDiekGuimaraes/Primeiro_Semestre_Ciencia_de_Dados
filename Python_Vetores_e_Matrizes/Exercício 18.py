"""18 - Concatene duas matrizes horizontalmente. Dica: use np.hstack()
Exemplo: matriz_1 = ([1,2,3],[4,5,6]) matriz_2([7,8,9],[10,11,12])
Matriz concatenada [[1,2,3,7,8,9],[4,5,6,10,11,12]]"""
import numpy as np
matriz_1 = ([1, 2, 3], [4, 5, 6])
matriz_2 = ([7, 8, 9], [10, 11, 12])
matriz_concatenada = np.hstack((matriz_1, matriz_2))
print(matriz_concatenada)
