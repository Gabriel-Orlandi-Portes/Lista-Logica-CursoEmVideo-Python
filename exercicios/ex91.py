def Maior(n1, n2):
    if n1 > n2:
        print(f'Primeiro valor ({n1}) maior que o segundo ({n2})')
    elif n1 < n2:
        print(f'Segundo valor ({n2}) maior que o primeiro ({n1})')
    else:
        print('Números iguais!')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

Maior(n1, n2)