km = int(input('Digite a quantidade de KM percorrido: '))
dias = int(input('Digite a quantidade de dias que o carro ficou alugado: '))

total = (dias * 90) + (km * 0.2)

print(f'O valor total ficou em R${total:.2f}')