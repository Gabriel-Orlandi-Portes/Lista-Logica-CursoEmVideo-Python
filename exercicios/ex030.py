l1 = int(input('Digite o valor do primeiro segmento: '))
l2 = int(input('Digite o valor do segundo segmento: '))
l3 = int(input('Digite o valor do terceiro segmento: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo')

    if l1 == l2 and l1 == l3:
        print('TRIÂNGULO EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('TRIÂNGULO ISÓSCELES')
    else:
        print('TRIÂNGULO ESCALENO')
else:
    print('Não é possível formar um triângulo')