# 17 - Implemente uma função que retorne a quantidade de dígitos de um determinado número natural passado como argumento.

def quantidade_digitos(numero):
    numero_str = str(numero)
    return len(numero_str)

quantidade_digitos(5000)