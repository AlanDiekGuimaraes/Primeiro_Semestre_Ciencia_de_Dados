"""19 - Encontre o produto escalar entre os vetores [1, 2, 3] e [4, 5, 6]. Dica: use np.dot() e
também o operador @ para conferir o outro resultado"""
import numpy as np
vetor1 = np.array([1, 2, 3])
vetor2 = np.array([4, 5, 6])
prod_escalar0 = vetor1.dot(vetor2)
prod_escalar1 = vetor1 @ vetor2

print(f"""produto escalar 0: {prod_escalar0}
produto escalar 1: {prod_escalar1}""")
