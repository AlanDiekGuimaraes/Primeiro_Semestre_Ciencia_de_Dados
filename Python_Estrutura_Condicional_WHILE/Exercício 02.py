# 2. Faça um programa que calcule o mostre a média aritmética de N notas.

contador = 0
nota = 0
soma = 0
contador_digitadas = 0
contador_digitadas = int(input("Digite a quantidade de notas a serem inseridas: "))
while contador < contador_digitadas :
  nota = int(input("Digite o valor da nota: "))
  contador += 1
  soma += nota

print(f"O soma total é: {soma} e a média é {soma/contador_digitadas}")
