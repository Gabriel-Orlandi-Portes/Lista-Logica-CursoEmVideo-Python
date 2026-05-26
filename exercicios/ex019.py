nome = input('Digite seu nome: ')
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1+n2) / 2

print(f'Olá {nome}, a sua média é {media} ')

if media >= 7:
    print('Parabéns, você ficou acima da média')
else:
    print('Você ficou abaixo da média')