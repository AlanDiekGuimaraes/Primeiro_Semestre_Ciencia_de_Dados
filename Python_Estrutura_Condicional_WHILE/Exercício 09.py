# 9. A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
n_numeros = int(input("Digite um número para calcularmos sua sequencia Fibonacci: "))
contador = 0
primeiro = 1
segundo = 1
soma = 0

while contador < n_numeros:
 print(primeiro)
 soma = primeiro + segundo
 primeiro = segundo
 segundo = soma
 contador +=1