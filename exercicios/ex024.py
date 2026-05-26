dist = int(input('Digite a distância da corrida: '))

if dist <= 200:
    valor = dist * 0.5
    print(f'O valor da corrida é R${valor}')
else:
    valor = dist * 0.45
    print(f'O valor da corrida é R${valor}')