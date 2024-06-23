"""
6. Cálculo de média móvel (como eram construídos os gráficos na pandemia)
Escreva uma função que recebe uma lista de números e um tamanho de janela como
entrada. A função deve calcular a média móvel dos números em cada janela deslizante
usando uma fila. Por exemplo, se a lista for

[3, 5, 7, 10, 6, 4, 5, 8, ...]

e o tamanho da janela for 3, a média móvel seria

[5.00, 7.33, 7.67, 6.67, 5.00, 5.67, ...]

Note:
5.00 = (3 + 5 + 7) / 3
7.33 = (5 + 7 + 10) / 3
7.67 = (7 + 10 + 6) / 3
6.67 = (10 + 6 + 4) / 3
5.00 = (6 + 4 + 5) / 3
5.67 = (4 + 5 + 8) / 3
"""

import queue

def media_movel(sequencia, janela):
    fila = queue.Queue()
    soma = 0
    media_movel_ov = []
    for i, n in enumerate(sequencia):
        fila.put(n)
        soma += n
        if i >= janela-1:
            media_movel_ov.append(soma/janela)
            soma -= fila.get()
    return media_movel_ov
            


valores = [3,5,7,10,6,4,5,8]
janela = 3
print(media_movel(valores, janela))