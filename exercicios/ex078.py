vetor = []
posicoes = []

for i in range(15):
    n1 = int(input(f'Digite o {i + 1}º número: '))
    vetor.append(n1)

    if n1 % 10 == 0:
        posicoes.append(i)

print(vetor)
print(posicoes)
