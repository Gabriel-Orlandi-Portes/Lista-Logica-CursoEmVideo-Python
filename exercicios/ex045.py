valor_inicial = int(input('Digite o valor inicial do loop: '))
valor_final = int(input('Digite o valor final do loop: '))
incremento = int(input('Digite o incremento do loop: '))

if incremento == 0:
    print('Valores incorretos')
elif valor_inicial < valor_final and incremento < 0:
    print('Valores incorretos')
elif valor_inicial > valor_final and incremento > 0:
    print('Valores incorretos')
else:
    for i in range(valor_inicial, valor_final + 1, incremento):
        print(i)
    print('Acabou!')