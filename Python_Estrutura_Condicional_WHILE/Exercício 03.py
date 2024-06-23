# 3. Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

usuario = input("Digite o nome do usuário: ")
senha = input("Digite sua senha: ")
while usuario == senha:
  print("Senha invalida, a senha não pode ser o nome de usuario")
  senha = str(input("Digite sua senha: "))
print("Senha valida")