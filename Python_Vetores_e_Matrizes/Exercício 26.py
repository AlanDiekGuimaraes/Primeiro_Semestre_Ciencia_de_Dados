"""26 - Dada a matriz A, encontre sua inversa A
−1
Então, comprove que A A
−1 = I, onde I é
a matriz identidade, com elementos da diagonal unitários e o restante zero.
"""
import numpy as np
# Criando array
a = np.array([[1, 3, 2], [5, 4, 6], [7, 9, 8]])
# Usando o parâmetro .inv(), no qual transforma os valores para o inverso.
b = np.linalg.inv(a)
# Verificando o Identificador com .dot
c = np.fix(np.round(b @ a))

print(b)
print(c)