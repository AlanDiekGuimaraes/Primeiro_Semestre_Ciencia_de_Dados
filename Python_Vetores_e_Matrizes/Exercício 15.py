"""
15 - Adicione um valor constante a todos os elementos de um vetor.
Exemplo: Seja `vetor = np.array([1, 2, 3, 4])` e `constante = 5`, o resultado seria array([6, 7, 8, 9])
"""
import numpy as np
vetor = np.array([1, 2, 3, 4])
constante = 5
vetor = vetor + constante
print(vetor)
