atleta = {
    'nome': '',
    'notas': [],
    'média': 0
}

atleta['nome'] = input('Digite o nome do atleta: ').title()

atleta['notas'] = [float(input('Digite a nota do salto: ')) for i in range(7)]
atleta['notas'].sort()
atleta['notas'].pop(0)
atleta['notas'].pop()

atleta['média'] = sum(atleta['notas']) / len(atleta['notas'])

print(f'\nNome do atleta: {atleta["nome"]}\nNotas: {atleta["notas"]}\nMédia: {atleta["média"]:.2f}')