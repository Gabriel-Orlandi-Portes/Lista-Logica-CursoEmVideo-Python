i = 0
soma = 0
maior_de_18 = 0
menor_de_5 = 0
maior_idade = 0

while i < 10:
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))

    soma += idade

    if idade > 18:
        maior_de_18 += 1 
    
    if idade < 5:
        menor_de_5 += 1
    
    if idade > maior_idade:
        maior_idade = idade
    
    i += 1

media = soma / 10

print(f'A - A média de idade do grupo é {media:.1f}')
print(f'B - {maior_de_18} pessoas tem mais de 18 anos')
print(f'C - {menor_de_5} pessoas tem menos de 5 anos')
print(f'D - A maior idade registrada foi {maior_idade}')

