# 8. Faça um programa que solicite ao usuário números indefinidamente até que ele
# digite 0. Em seguida, o programa deve imprimir a média dos números digitados.

contador = 0
soma = 0
numero = int(input("Digite um número qualquer : "))
soma = soma + numero
while numero != 0:
 numero = int(input("Digite um número qualquer : "))
 soma = soma + numero
 contador += 1
if soma > 0:
  print(f"A media dos numeros digitados é {soma / contador:.21f}")