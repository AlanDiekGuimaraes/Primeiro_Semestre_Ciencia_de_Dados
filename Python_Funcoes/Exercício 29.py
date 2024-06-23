# 29 - Função Lambda
quadrado = lambda x: x**2
print(quadrado(3))

celsiusXfahrenheit = lambda c: c*1.8+32

print(celsiusXfahrenheit(100))

"Função para retornar o maior elemento entre o intervalo de valores entre a e b"

max = lambda a, b: a if a>b else b

print(max(100, 90))

print((lambda a, b: a if a>b else b)(100, 90))