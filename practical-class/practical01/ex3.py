tempo_execucao = int(input('Digite o tempo gasto(em segundos) pelo programa: '))

tempo_minutos = tempo_execucao // 60
resto_segundos = tempo_execucao % 60

tempo_horas = tempo_minutos // 60
resto_minutos = tempo_minutos % 60

print(tempo_horas, ' : ', resto_minutos, ' : ', resto_segundos)