# 05 - Função para calcular o perimetro.
def perimetro(altura,largura):
    total = (altura + largura)*2
    return total

altura = float(input("Insira a altura do retângulo: "))
largura = float(input("Insira a largura do retângulo: "))

perimetro(altura,largura)