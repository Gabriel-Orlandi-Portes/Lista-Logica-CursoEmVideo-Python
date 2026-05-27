nomes = []
idades = []

for i in range(9):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))

    nomes.append(nome)
    idades.append(idade)

print('Menores de idade:')

for i in range(9):
    if idades[i] < 18:
        print(f'{nomes[i]} - {idades[i]} anos')