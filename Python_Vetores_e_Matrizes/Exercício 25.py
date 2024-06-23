"""25 - Encontre a solução para o seguinte problema. Arredondar todos os valores em uma
matriz para o inteiro mais próximo. Dica: analise np.floor(), np.ceil(), np.fix() e np.round()
Exemplo:
"""
import numpy as np
# Criando array
matriz = np.array([[1.2, 2.8, 3.5], [4.9, 5.1, 6.7], [7.3, 8.6, 9.2]])
# Imprimindo Matriz Original
print(f'Matriz Original\n{matriz}\n')
# Floor - Análise para baixo independente do valor, mas se mantem decimal.
floor = np.floor(matriz)
# Ceil - Análise para cima se o decimal for maior que 0.
ceil = np.ceil(matriz)
# Fix - Desconsidera todos os valores decimais e trunca o elemento.
fix = np.fix(matriz)
# Round - Arredonda o valor de acordo com o decimal: Acima de 5 arredonda para cima, vice-versa.

round = np.round(matriz)
# Imprimindo valores
print(f'Usando floor:\n {floor}\n\n',
      f'Usando ceil:\n {ceil}\n\n',
      f'Usando fix:\n {fix}\n\n',
      f'Usando round:\n {round}')