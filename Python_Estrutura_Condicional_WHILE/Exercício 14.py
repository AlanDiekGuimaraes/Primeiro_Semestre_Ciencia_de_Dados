# 14 - Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1 trocando o sinal dos números. Realizar o exercício usando loops for e while. Exemplo para N igual a 5:
#Resultado intercalados entre negativos e positivos
N = int(input('Digite um valor maior que 1: '))
mult = -1
fat = -1

#FOR Decrecente
print('For Decrecente:', end=' ')
for n in range(N):
    num = fat * (N-n)
    fat *= mult
    print(num, end=' ')
print()

#FOR Crecente
print('For Crecente:', end=' ')
for n in range(N):
    num = fat * n
    fat *= mult
    print(num, end=' ')
print()


#WHILE
print('While decrecente :', end=' ')
mult = -1
fat = 1
contador = 0
while contador < N:
    num = fat * (N-contador)
    fat *= mult
    contador+=1
    print(num, end=' ')
print()

#WHILE
print('While crecente :', end=' ')
mult = -1
fat = 1
contador = 0
while contador < N:
    num = fat * contador
    fat *= mult
    contador+=1
    print(num, end=' ')