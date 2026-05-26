horas = int(input('Digite quantas horas você teve no mês? '))

if horas < 10:
    pontos = horas * 2
    ganho = pontos * 0.05
    print(f'Parabéns, você treinou durante {horas} horas, ganhou {pontos} pontos e acumulou R${ganho:.2f}.')
elif horas < 20:
    pontos = horas * 5
    ganho = pontos * 0.05
    print(f'Parabéns, você treinou durante {horas} horas, ganhou {pontos} pontos e acumulou R${ganho:.2f}.')
else:
    pontos = horas * 10
    ganho = pontos * 0.05
    print(f'Parabéns, você treinou durante {horas} horas, ganhou {pontos} pontos e acumulou R${ganho:.2f}.')