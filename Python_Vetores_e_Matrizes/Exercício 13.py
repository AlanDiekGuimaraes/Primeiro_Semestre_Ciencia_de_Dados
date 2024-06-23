"""
13 - Substitua todos os valores negativos em um vetor por 0. Exemplo: Seja `vetor = np.array([-1, 2, -3, 4, -5])`,
o resultado seria `array([0, 2, 0, 4, 0])
"""
import numpy as np
vetor = np.array([-1, 2, -3, 4, -5])
vetor[vetor < 0] = 0
print(vetor)
