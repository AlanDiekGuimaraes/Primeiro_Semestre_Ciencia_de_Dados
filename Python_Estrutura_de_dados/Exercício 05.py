"""
5. Avaliação de Expressões Pós-fixa (ou Notação Polonesa Reversa)
Descrição: crie um programa Python que avalie uma expressão matemática na forma
pós-fixa (ou notação polonesa reversa) usando uma pilha. A expressão pós-fixa é uma
notação onde os operadores seguem seus operandos e dispensa parênteses.
Entrada: "2 3 + 5 *"
Resultado: 25 (resultado da expressão)
Entrada: " 7 4 – 3 * 16 2 / -"
Resultado: 1 (resultado da expressão)

Dica de Implementação:
1. Divida a expressão em tokens separados por espaços.
2. Percorra os tokens da expressão.
3. Se encontrar um operando (número), empilhe-o.
4. Se encontrar um operador, desempilhe dois operandos, aplique o operador e empilhe
o resultado.
5. No final, o resultado estará no topo da pilha. 
"""

import queue

operador = {"+": lambda op1, op2: op1+op2,
            "-": lambda op1, op2: op1-op2,
            "*": lambda op1, op2: op1*op2,
            "/": lambda op1, op2: op1/op2,
    }
def avalia(expressao):
    pilha = queue.LifoQueue()
    tokens = expressao.split()
    
    for tk in tokens:
        if tk.isdigit():
            pilha.put(float(tk))
        elif tk in operador:
            op2 = pilha.get()
            op1 = pilha.get()
            resultado = operador[tk](op1, op2)
            pilha.put(resultado)
    return pilha.get()
                
expressao = "7 4 - 3 * 16 2 / -"
print(avalia(expressao))