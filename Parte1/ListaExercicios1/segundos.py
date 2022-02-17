segundos_str = input(
    'Por favor, entre com o número de segundos que deseja converter:')
total_segs = int(segundos_str)

dias = total_segs // (3600*24)
horas = total_segs % (3600*24) // 3600
minutos = (total_segs % 3600) // 60
segundos = ((total_segs % 3600) % 60)

print(dias, 'dias,', horas, 'horas,', minutos,
      'minutos e', segundos, 'segundos.')
