    i = 0

    soma_alt= 0
    mais_90 = 0
    menos_50 = 0
    mais_100 = 0

    while i < 7:
        altura = float(input(f'Digite a altura da {i+1} pessoa: '))

        while altura <= 0 or altura > 3:
            altura = float(input('Digite uma entrada válida: '))
        
        peso = float(input(f'Digite o peso da {i+1} pessoa: '))

        soma_alt += altura

        if peso > 90:
            mais_90 += 1
        
        if peso < 50 and altura < 1.6:
            menos_50 += 1
        
        if peso > 100 and altura > 1.9:
            mais_100 += 1

        i += 1

    media_altura = soma_alt / 7

    print(f'A - A média de altura do grupo é {media_altura:.1f}m')
    print(f'B - {mais_90} pessoas pesam mais de 90 kg')
    print(f'C - {menos_50} pessoas pesam menos de 50 kg e tem menos de 1.60m')
    print(f'D - {mais_100} pessoas pesam mais de 100 kg e tem mais de 1.90m')