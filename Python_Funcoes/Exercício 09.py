# 09 - Criar uma calculadora em python

# Calculadora em python
def cabecalho(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def rodape(mensagem):
    print("=" * 50)
    print(mensagem.center(50).upper())
    print("=" * 50)


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    return num1 / num2


def potenciacao(num1, num2):
    return num1 ** num2


# Função para exibir o menu da calculadora
def exibir_menu():
    print("Escolha a operação - Calculadora".center(50).upper())
    print(f"""1. soma
2. subtração
3. Multiplicação
4. Divisão
5. Potenciacão""")
    print("-" * 50)


# Função principal da calculadora

def calculadora():
    exibir_menu()
    opcao = int(input("Digite o número da operação desejada: "))
    resposta = 0

    if opcao in (1, 2, 3, 4, 5):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o Segundo número: "))
        if opcao == 1:
            resposta = soma(num1, num2)

        if opcao == 2:
            resposta = subtracao(num1, num2)

        if opcao == 3:
            resposta = multiplicacao(num1, num2)
        if opcao == 4:
            if num2 == 0:
                return print("Divisão invalida")
            resposta = divisao(num1, num2)
        if opcao == 5:
            resposta = potenciacao(num1, num2)

        print(f"Resposta: {resposta:.2f}")
    else:
        print("Opção invalida")

cabecalho(mensagem="calculadora em python")
calculadora()
rodape(mensagem="fim do programa")

