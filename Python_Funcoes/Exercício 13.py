# 13 - Implemente uma função que receba um valor n inteiro e imprima ate a n-ésima linha da seguinte forma.
#  1
#  2 2
#  3 3 3

def alinhamento(n):
    for i in range(n):
        print(f" {i}"*i, end=" " )
        print("")
alinhamento(10)