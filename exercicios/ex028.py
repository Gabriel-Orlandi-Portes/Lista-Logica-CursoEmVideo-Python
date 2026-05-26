larg = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))

area = larg * comp

if area < 100:
    print(f'Área de {area}M² --> TERRENO POPULAR')
elif area < 500:
    print(f'Área de {area}M² -->TERRENO MASTER')
else:
    print(f'Área de {area}M² -->TERRENO VIP  ')