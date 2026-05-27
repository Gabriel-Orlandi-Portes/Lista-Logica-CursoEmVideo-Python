vetor = []
pares = []

for i in range(10):
    n1 = int(input(f'Digite o {i+1}º número: '))
    if n1 % 2 == 0:
        pares.append(i)
        vetor.append(n1)

print(f'Os números pares digitados foram {vetor}')
print(f'A posição desses números: {pares}')
