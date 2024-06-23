# 10 - Criar código validador de CPF
# Validador de CPF

def cabecalho(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def rodape(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def validar_digito_verificador_1(digitos):
    soma_digito_1 = 0
    for n in range(9):
        soma_digito_1 += (digitos[n] * (10 - n))
    d1 = ((soma_digito_1 * 10) % 11) % 10
    return d1 == digitos[-2]


def validar_digito_verificador_2(digitos):
    soma_digito_2 = 0
    for n in range(10):
        soma_digito_2 += (digitos[n] * (11 - n))
    d2 = ((soma_digito_2 * 10) % 11) % 10
    return d2 == digitos[-1]


def validar_cpf(cpf):
    cpf_n = [int(digito) for digito in cpf if digito.isdigit()]
    v1 = validar_digito_verificador_1(cpf_n)
    if len(set(cpf_n)) == 1:
        return False
    if v1 == False:
        return False
    v2 = validar_digito_verificador_2(cpf_n)
    if v2 == True:
        return True
    else:
        return False


def main():
    cpf = input("Digite o CPF (Apenas números): ")
    if validar_cpf(cpf):
        print(f"{cpf} :CPF válido!")
    else:
        print(f"{cpf} : CPF inválido")

cabecalho(mensagem="Validador de cpf")
main()
rodape(mensagem="Fim do programa")
