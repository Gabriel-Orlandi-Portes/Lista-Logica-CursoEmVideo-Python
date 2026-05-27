def Contador(inicio, fim, incremento):
    for i in range(inicio, fim + 1, incremento):
        print(i, end=' >> ')
    print('FIM')

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o incremento: '))

Contador(i, f, p)
    