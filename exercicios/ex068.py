qtde_mulheres = 0
soma_peso_mulheres = 0
homem_100 = 0
maior_peso_homem = 0
tem_homem = False

for i in range(8):
    sexo = input(f'Digite o sexo da {i+1} pessoa (m ou f): ').lower()
    
    while sexo not in ['m', 'f']:
        sexo = input(f'Digite o sexo da {i+1} pessoa (m ou f): ').lower()
    
    peso = float(input(f'Digite o peso da {i+1} pessoa: '))

    if sexo == 'f':
        qtde_mulheres += 1
        soma_peso_mulheres += peso
    else:
        tem_homem = True
        if peso > 100:
            homem_100 += 1

        if peso > maior_peso_homem:
            maior_peso_homem = peso

if qtde_mulheres > 0:
    media_peso_mulher = soma_peso_mulheres / qtde_mulheres
else:
    media_peso_mulher = 0

print(f'A - Foram cadastradas {qtde_mulheres} mulheres')
print(f'B - {homem_100} homens pesam mais de 100 kg')
print(f'C - A média de peso entre as mulheres é igual a {media_peso_mulher:.2f} kg')

if tem_homem:
    print(f'D - O maior peso entre os homens é {maior_peso_homem} kg')
else:
    print('D - Não foram cadastrados homens')