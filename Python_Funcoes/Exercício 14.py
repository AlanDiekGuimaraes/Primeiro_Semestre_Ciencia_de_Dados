# 14 - Implemente uma função que receba um valor n inteiro e imprima até a n-ésima linha da seguinte forma:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def alinhamento2(n):
    for i in range(1, n + 1):
        for _ in range(1, i + 1):
            print(f"{_}", end=" ")
        print()


alinhamento2(5)