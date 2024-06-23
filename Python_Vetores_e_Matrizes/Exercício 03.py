"""
03 - Implemente a função transp(mat) que recebe uma matriz mat e retorna sua transposta.
"""


def transp(mat):
    num_linhas = len(mat)
    num_colunas = len(mat[0])
    transposta = [[0 for linha in range(num_linhas)]
                  for coluna in range(num_colunas)]
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            transposta[coluna][linha] = mat[linha][coluna]
    return transposta


resposta = transp([[1, 2, 3], [4, 5, 6]])
print(resposta)
