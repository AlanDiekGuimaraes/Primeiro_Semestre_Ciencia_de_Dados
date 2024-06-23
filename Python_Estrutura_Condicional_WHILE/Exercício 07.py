# 7. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um numero para calcularmos seu fatorial: "))
resultado = 1
numero_inicial = numero
while numero != 0:
  resultado *= numero
  numero -=1

print(f"O fatorial de {numero_inicial} é {resultado}")
