nomes = []
sexos = []
salarios = []

for i in range(5):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    sexo = input(f'Digite o sexo da {i+1}ª pessoa (M ou F):').lower()
    while sexo not in ['m', 'f']:
        sexo = input(f'Digite o sexo da {i+1}ª pessoa (M ou F):').lower()
    
    salario = float(input(f'Digite o salário da {i+1}ª pessoa:'))


    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

print('funcionárias que ganham mais de R$5 mil: ')

for i in range(5):
    if sexos[i] == 'f' and salarios[i]:
        print(nomes[i])
