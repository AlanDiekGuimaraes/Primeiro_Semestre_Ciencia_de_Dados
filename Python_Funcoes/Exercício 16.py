# 16 - Implemente uma função que retorne True se o argumento de entrada for um número natural primo e False caso contrário.

def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


e_primo(-7)