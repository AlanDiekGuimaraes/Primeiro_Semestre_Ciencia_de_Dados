# 11 - Geração dos 2 ultimos digitos do CPF

def cabecalho(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def rodape(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def gerar_digito_verificador_1(digitos):
    copia_d1 = digitos.copy()
    soma_digito_1 = 0
    for n in range(9):
        soma_digito_1 += (digitos[n] * (10 - n))
    d1 = ((soma_digito_1 * 10) % 11) % 10
    copia_d1.append(d1)
    return copia_d1


def gerar_digito_verificador_2(digitos):
    copia_d2 = digitos.copy()
    soma_digito_2 = 0
    for n in range(10):
        soma_digito_2 += (digitos[n] * (11 - n))
    d2 = ((soma_digito_2 * 10) % 11) % 10
    copia_d2.append(d2)
    return copia_d2


def gerar_cpf(cpf):
    cpf_final = ""
    cpf_n = [int(digito) for digito in cpf if digito in cpf if digito.isdigit()]
    resultado1 = gerar_digito_verificador_1(cpf_n)
    resultado2 = gerar_digito_verificador_2(resultado1)
    if len(set(cpf_n)) == 1:
        return "inválido"
    for n in resultado2:
        cpf_final += str(n)
    return cpf_final


def main():
    cpf = input("Digite os 9 digitos do CPF: ")
    print(f"Valores digitados: {cpf}")
    print(f"C.P.F.: {gerar_cpf(cpf)}")


cabecalho("Gerador de CPF")
main()
rodape("Fim do programa")