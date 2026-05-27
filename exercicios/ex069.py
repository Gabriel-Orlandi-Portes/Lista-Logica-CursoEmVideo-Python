primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

soma = 0
termo = primeiro_termo

for i in range(10):
    print(termo)
    soma += termo
    termo += razao

print('Soma:', soma)