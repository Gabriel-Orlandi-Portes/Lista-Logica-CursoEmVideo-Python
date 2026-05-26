qtde_cigarros_dia = int(input('Digite a quantidade de cigarros que você fuma por dia: '))
qtde_anos = int(input('Digite a quantidade de anos que você fuma: '))

tempo_perdido = qtde_cigarros_dia * 10
minutos_perdidos = tempo_perdido * 365 * qtde_anos
dias_perdidos = minutos_perdidos / 1440

print(f'Você perdeu aproximadamente {dias_perdidos:.0f} dias de vida.') 