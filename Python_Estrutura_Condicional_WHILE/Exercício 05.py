# 5. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite Seu nome: "))
while (len(nome)) < 3:
  print("Seu nome deve ter mais de 3 caracteres")
  nome = str(input("Digite Seu nome: "))

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
  print("Idade invalida")
  idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
  print("Salario 0 é Inválido")
  salario = float(input("Digite seu salário: "))

sexo = str(input("Digite seu sexo F ou M: "))
while (sexo != "M" and sexo != "F" and sexo != "m" and sexo != "f"):
  print("Dados inválidos")
  sexo = str(input("Digite seu sexo F ou M: "))

estado_civil = str(input('''
Digite seu estado civil com:
S para solteiro
C para casado
V para viúvo
D para divorciado ''')).lower()

while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
  print("Dados inválidos")
  estado_civil = str(input('''
Digite seu estado civil com:
S para solteiro
C para casado
V para viúvo
D para divorciado ''')).lower()

print(f'''
Seu nome é: {nome}
Sua idade é: {idade}
Seu sexo é: {sexo}
Seu salário é: {salario}
Seu estado civil é: {estado_civil}
''')