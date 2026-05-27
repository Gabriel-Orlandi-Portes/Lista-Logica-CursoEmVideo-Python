contador = 0
soma = 0
maiores_de_21 = 0

while True:
    idade = int(input('Digite uma idade: '))
    contador += 1
    soma += idade

    if idade >= 21:
        maiores_de_21 += 1

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

media = soma / contador

print(f'A - Foram digitadas {contador} idades')
print(f'B - A média das idades é {media}')
print(f'C - {maiores_de_21} pessoas têm 21 anos ou mais')