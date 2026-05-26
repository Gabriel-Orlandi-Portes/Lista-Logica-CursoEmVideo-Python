genero = input('Digite seu sexo (M ou F): ').lower()
salario_atual = float(input('Digite seu salário atual: R$'))
qtde_anos = int(input('Digite a quantidade de anos que você está na empresa: '))

genero_correto = ['m', 'f']

if genero not in genero_correto:
    print('Gênero inválido')
elif genero == 'm':
    if qtde_anos < 20:
        novo_salario = salario_atual * 1.03
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')
    elif qtde_anos < 30:
        novo_salario = salario_atual * 1.13
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')
    else:
        novo_salario = salario_atual * 1.25
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')
else:
    if qtde_anos < 15:
        novo_salario = salario_atual * 1.05
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')
    elif qtde_anos < 20:
        novo_salario = salario_atual * 1.12
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')
    else:
        novo_salario = salario_atual * 1.23
        print(f'Olá, com base na quantidade de anos na empresa, seu novo salário sera de R${novo_salario}')