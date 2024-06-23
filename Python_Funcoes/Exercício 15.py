# 15 - Implemente uma função que receba um valor em segundos e imprima o correspondente em horas, minutos e segundos. Por exempli, se a função receber como argumento 4814, imprimirá
# 1 hora(s) 20 minuto(s) e 14 segundo(s).

def converter_segundos(segundos):
    horas = segundos // 3600
    segundos2 = segundos % 3600
    minutos = segundos2 // 60
    segundos2 = segundos2 % 60

    print(f"{horas} hora(s), {minutos} minuto(s) e {segundos2} segundo(s)")
converter_segundos(4814)