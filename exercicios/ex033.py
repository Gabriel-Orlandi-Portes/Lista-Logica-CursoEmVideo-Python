valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
anos = int(input('Digite em quantos anos você irá pagar: '))

total_meses = anos * 12
valor_mensal = valor_casa / total_meses

if valor_mensal > 0.3 * salario:
    print('EMPRÉSTIMO NEGADO')
else:
    print(f'EMPRÉSTIMO ACEITO. PRESTAÇÃO MENSAL: {valor_mensal}')