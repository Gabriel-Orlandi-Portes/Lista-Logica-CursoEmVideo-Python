velo = int(input('Digite a velocidade do carro: '))

if velo > 80:
    multa = (velo - 80) * 5
    print(f'Você foi multado em R${multa:.2f}')