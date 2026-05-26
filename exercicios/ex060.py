maior_idade = 0
nome_mais_velho = ''

menor_idade_mulher = 0
nome_mulher_mais_jovem = ''

soma_idades = 0
total_pessoas = 0

homens_mais_30 = 0
mulheres_menos_18 = 0

while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M ou F): ').lower()

    while sexo not in ['m', 'f']:
        sexo = input('Digite o sexo (M ou F): ').lower()

    soma_idades += idade
    total_pessoas += 1

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

    if sexo == 'f':
        if menor_idade_mulher == 0 or idade < menor_idade_mulher:
            menor_idade_mulher = idade
            nome_mulher_mais_jovem = nome

        if idade < 18:
            mulheres_menos_18 += 1

    if sexo == 'm' and idade > 30:
        homens_mais_30 += 1

    continuar = input('Deseja continuar (S ou N)? ').lower()
    while continuar not in ['s', 'n']:
        continuar = input('Deseja continuar (S ou N)? ').lower()

    if continuar == 'n':
        break

media_idade = soma_idades / total_pessoas

# resultados
print(f'\nPessoa mais velha: {nome_mais_velho}')
print(f'Mulher mais jovem: {nome_mulher_mais_jovem}')
print(f'Média de idade do grupo: {media_idade:.2f}')
print(f'Homens com mais de 30 anos: {homens_mais_30}')
print(f'Mulheres com menos de 18 anos: {mulheres_menos_18}')