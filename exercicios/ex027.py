n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Média final: {media} \nStatus: REPROVADO')
elif media < 7:
    print(f'Média final: {media} \nStatus: RECUPERAÇÃO')
else:
    print(f'Média final: {media} \nStatus: APROVADO')