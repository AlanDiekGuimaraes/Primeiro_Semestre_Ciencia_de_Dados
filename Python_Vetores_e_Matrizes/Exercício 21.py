"""21 - Calcule a média e o desvio padrão de cada coluna de uma matriz. Dica: use np.mean()
e np.std(). Exemplo: matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). O resultado deve ser:
média por coluna: [4. 5. 6.], desvio padrão por coluna: [2.4495, 2.4495, 2.4495]"""
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dp = np.mean(matriz, axis=0)
md = np.std(matriz, axis=0)
print(f"Desvio padrão: {dp}")
print(f"Média: {md}")
