"""20 - Calcule a média e o desvio padrão de cada linha de uma matriz. Dica: use np.mean() e
np.std(). Exemplo: `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`. O resultado deve ser:
média por linha: [2. 5. 8.], desvio padrão por linha: [0.8165, 0.8165, 0.8165]"""
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dp = np.mean(matriz, axis=1)
md = np.std(matriz, axis=1)
print(f"Desvio padrão: {dp}")
print(f"Média: {md}")
