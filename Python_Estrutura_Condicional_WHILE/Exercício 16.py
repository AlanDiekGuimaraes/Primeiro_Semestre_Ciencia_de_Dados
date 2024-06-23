# 16 - Solicitar um número inteiro positivo N ao usuário e imprimir i^2 para ) < i < N.
# Por exemplo, para N = 5, serão impressos: 1, 4, 9, 16.

N = int(input('Digite um número maior que 1: '))

#FOR
print('For: ')
for contador in range(1, N):
      print(contador * contador)
print()

#WHITE
print('While: ')
contador = 1
while contador < N:
    print(contador * contador)
    contador += 1
print()