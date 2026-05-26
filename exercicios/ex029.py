nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: R$'))
anos = int(input('Digite quantos anos você trabalha na empresa: '))

if anos < 3:
    novo_salario = salario * 1.03
    print(f'Olá {nome}, você possui {anos} anos de empresa, e o seu salário foi de R${salario:.2f} para R${novo_salario:.2f}')
elif anos < 10:
    novo_salario = salario * 1.125
    print(f'Olá {nome}, você possui {anos} anos de empresa, e o seu salário foi de R${salario:.2f} para R${novo_salario:.2f}')
else:
    novo_salario = salario * 1.2
    print(f'Olá {nome}, você possui {anos} anos de empresa, e o seu salário foi de R${salario:.2f} para R${novo_salario:.2f}')