i = 0

qtde_homens = 0
qtde_mulheres = 0
soma_grupo = 0
soma_homens = 0
mulheres_20 = 0

while i < 5:
    sexo = input(f'Digite o sexo da {i+1}ª pessoa (M ou F): ').lower()

    while sexo not in ['m', 'f']:
        sexo = input('Entrada inválida! Digite M ou F: ').lower()

    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))

    if sexo == 'm':
        qtde_homens += 1
        soma_homens += idade
    else:
        qtde_mulheres += 1
        if idade > 20:
            mulheres_20 += 1

    soma_grupo += idade
    i += 1

media_grupo = soma_grupo / 5

if qtde_homens > 0:
    media_homens = soma_homens / qtde_homens
else:
    media_homens = 0

print(f'A - {qtde_homens} homens foram cadastrados')
print(f'B - {qtde_mulheres} mulheres foram cadastradas')
print(f'C - A média de idade do grupo é de {media_grupo:.1f} anos')
print(f'D - A média de idade dos homens é de {media_homens:.1f} anos')
print(f'E - {mulheres_20} mulheres possuem mais de 20 anos')