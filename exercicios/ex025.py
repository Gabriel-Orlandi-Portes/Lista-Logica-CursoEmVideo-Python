l1 = int(input('Digite o valor do primeiro segmento: '))
l2 = int(input('Digite o valor do segundo segmento: '))
l3 = int(input('Digite o valor do terceiro segmento: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')