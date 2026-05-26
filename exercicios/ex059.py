
maior_idade = 0
cadastro_homens = 0
mulher_mais_jovem = None
soma_homens = 0


while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M ou F): ').lower()

    while sexo not in ['m', 'f']:
        sexo = input('Digite o sexo (M ou F): ').lower()

    if idade > maior_idade:
        maior_idade = idade
    
    if sexo == 'm':
        cadastro_homens += 1
        soma_homens += idade
    else:
        if mulher_mais_jovem is None or idade < mulher_mais_jovem:
            mulher_mais_jovem = idade

    continuar = input('Deseja continuar (S ou N)? ').lower()
    while continuar not in ['s', 'n']:
        continuar = input('Deseja continuar (S ou N)? ').lower()
    
    if continuar == 'n':
        break

media_homens = soma_homens / cadastro_homens

print(f'A maior idade lida é {maior_idade}')
print(f'{cadastro_homens} homens foram cadastrados')
print(f'A idade da mulher mais jovem é {mulher_mais_jovem} anos')
print(f'A média de idade dos homene é {media_homens}')