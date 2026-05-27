contador = 0
soma = 0
menor = None
par = 0

while True:
    n1 = int(input('Digite um número: '))
    contador += 1
    soma += n1

    if menor is None or n1 < menor:
        menor = n1

    if n1 % 2 == 0:
        par += 1

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

media = soma / contador

print(f'A - O somatório dos valores é igual a {soma}')
print(f'B - O menor valor digitado foi {menor}')
print(f'C - A média entre os valores foi {media}')
print(f'D - {par} valores são pares')