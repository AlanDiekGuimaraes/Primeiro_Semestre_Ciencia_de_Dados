# 25 - Implemente uma função que recebe o seu peso e altura e retorna seu índice de massa corporal, IMC. A função também deverá emitir a classificação, de acordo com a tabela abaixo:
#      IMC           CLASSIFICAÇÃO
# MENOR QUE 18,5         MAGREZA
# ENTRE18,5 E 25,0       NORMAL
# ENTRE 25,0 E 30,0      SOBREPESO
# ENTRE 30,0 E 40,0      OBESIDADE
# MAIOR QUE 40,0         OBESIDADE GRAVE
# Dica

# IMC = peso/altura², peso em kg, altura em m
# peso, altura = 59, 1.64
# imc(peso, altura)
# IMC = 21.9
# Classificação = Obesidade

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        resultado = "Magreza"
    if imc <= 18.5 or imc <= 25:
        resultado = "normal"
    if imc <=25 or imc <30:
        resultado = "Spbrepeso"
    if imc <=30 or imc <40:
        resultado = "Obesidade"
    else:
        resultado = "Obesidade Grave"
    return f"{imc:.2f}", resultado

calcular_imc(59,1.64)