# 7. Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado; se a média for maior ou igual a 5 mas
# menor do que 7, informar que o aluno está de exame; se a média for menor do que 5 informar que o aluno foi reprovado


nota1 = int(input("Informe sua primeira nota"))

while nota1 < 0 or nota1 > 10:
  print("Nota inválida ")
  nota1 = int(input("Informe sua primeira nota"))

nota2 = int(input("Informe sua segunda nota"))

while nota2 < 0 or nota2 >10:
  print("Nota inválida ")
  nota2 = int(input("Informe sua segunda nota"))

media = (nota1 + nota2)/2

if media >= 7:
  print(f"Parabéns, você foi APROVADO, sua media foi {media}")
elif media < 5:
  print(f"Estude mais um pouco, você foi REPROVADO e sua media foi {media}")
else:
  print(f"Não foi dessa vez, você está em EXAME, sua media foi {media}")