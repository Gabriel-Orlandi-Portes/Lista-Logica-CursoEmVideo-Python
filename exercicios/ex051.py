maior_preco = 0
menor_preco = 0

i = 0

while i < 8:
    preco_atual = float(input(f'Digite o preço do {i+1}º produto: '))

    if i == 0:
        maior_preco = preco_atual
        menor_preco = preco_atual
    else:
        if preco_atual > maior_preco:
            maior_preco = preco_atual

        if preco_atual < menor_preco:
            menor_preco = preco_atual

    i += 1

print(f'Menor preço: {menor_preco}')
print(f'Maior preço: {maior_preco}')