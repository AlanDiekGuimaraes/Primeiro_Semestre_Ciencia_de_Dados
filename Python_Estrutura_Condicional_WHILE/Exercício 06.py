# 6. Supondo que a população de um país A seja da ordem de 80000 habitantes com
# uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.


populacaoA = 80000
populacaoB = 200000
crescimentoA = 0.03
crescimentoB = 0.015
aumentoA = 0
aumentoB = 0
anos = 0
while populacaoA <= populacaoB:

  aumentoA = populacaoA * crescimentoA
  populacaoA = aumentoA + populacaoA

  aumentoB = populacaoB * crescimentoB
  populacaoB = aumentoB + populacaoB

  anos += 1
print(f'''A quantidade de anos é: {anos} anos''')