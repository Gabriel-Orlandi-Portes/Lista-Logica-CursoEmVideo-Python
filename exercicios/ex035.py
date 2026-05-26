km = int(input('Digite a distância percorrida em km: '))
dias = int(input('Digite quantos dias você alugou o carro: '))
tipo = input('Digite o tipo de carro alugado (Popular ou luxo): ').lower()
tipos_de_carro = ['popular', 'luxo']

if tipo not in tipos_de_carro:
    print('tipo de carro inválido.') 
elif tipo == 'popular':
    if km <= 100:
        valor_final = (90 * dias) + (0.2 * km)
        print(f'O valor final é R${valor_final}')
    else:
        valor_final = (90 * dias) + ( 0.1 * km)
        print(f'O valor final é R${valor_final}')
else:
    if km <= 200:
        valor_final = (150 * dias) + (0.3 * km)
        print(f'O valor final é R${valor_final}')
    else:
        valor_final = (150 * dias) + (0.25 * km)
        print(f'O valor final é R${valor_final}')
