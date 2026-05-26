valor_inicial = int(input('Digite o valor inicial do loop: '))
valor_final = int(input('Digite o valor final do loop: '))
incremento = int(input('Digite o incremento do loop: '))

    for i in range(valor_inicial, valor_final + 1, incremento):
        print(i)
    print('Acabou!')