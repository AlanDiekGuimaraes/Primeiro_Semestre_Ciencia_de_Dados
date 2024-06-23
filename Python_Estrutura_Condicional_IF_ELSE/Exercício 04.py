# 4. Faça um programa que pergunte a temperatura atual para o usuário e mostre uma
# mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temperatura = int(input("Caro usuário, qual é a temperatura atual? "))

if  temperatura >= 28:
  print(f"{temperatura}°C é considerado quente.")
elif temperatura <= 20:
  print(f"{temperatura}°C é considerado frio")
else:
  print(f"{temperatura}°C é considerado agradável")