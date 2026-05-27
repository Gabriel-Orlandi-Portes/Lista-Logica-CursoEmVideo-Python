nomes = []


for i in range(7):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    nomes.append(nome)

print(nomes[::-1])