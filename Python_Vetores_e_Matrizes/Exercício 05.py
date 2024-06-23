"""
05 - Crie uma matriz numpy 3x3 com valores aleatórios entre 0 e 10. Dica: use np.random.rand()
"""

import numpy as np
arr = np.random.randint(low=0, high=10, size=(3, 3))
arr1 = np.random.rand(3, 3) * 10
print(f"{arr}")
print(f"{arr1}")
