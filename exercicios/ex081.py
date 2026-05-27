idades = []

soma = 0 
mais_25 = []
maior_idade = 0
posicoes_maior = []

for i in range(8):
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))

    idades.append(idade)
    
    soma += idade

    if idade > 25:
        mais_25.append(i)    

    if idade > maior_idade:
        maior_idade = idade

media = soma / 8

for i in range(len(idades)):
    if idades[i] == maior_idade:
        posicoes_maior.append(i)

print(f'Média das idades: {media}')
print(f'Posições com pessoas acima de 25 anos: {mais_25}')
print(f'Maior idade digitada: {maior_idade}')
print(f'Posições da maior idade: {posicoes_maior}')
