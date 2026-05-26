nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: F ou M').lower()
valor = float(input('Digite o valor da sua compra: R$'))

if sexo == 'f':
    desconto = valor * 0.87
    print(f'Olá {nome}, o valor da sua compra com o desconto fica em R${desconto}')
elif sexo == 'm':
    desconto = valor * 0.95
    print(f'Olá {nome}, o valor da sua compra com o desconto fica em R${desconto}')