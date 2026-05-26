i = 1

total_homens = 0
total_mulheres = 0 

while True:
    sexo = input('Digite o sexo do funcionário (M ou F): ').lower()

    while sexo not in ['m', 'f']:
        sexo = input('Sexo inválido! Digite M ou F: ').lower()
    
    salario = float(input(f'Digite o salário do {i}º funcionário: R$'))

    if sexo == 'm':
        total_homens += salario
    else:
        total_mulheres += salario
    
    continua = input('Você deseja continuar? (S/N): ').lower()

    if continua == 'n':
        break

    i += 1

print(f'Total pago aos homens: R${total_homens:.2f}')
print(f'Total pago às mulheres: R${total_mulheres:.2f}')