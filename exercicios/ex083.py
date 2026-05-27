import random

vetor = []

for i in range(20):
    num = random.randint(0, 99)
    vetor.append(num)

vetor_crescente = sorted(vetor)

print(f'Números gerados: {vetor}')
print(f'Números em ordem crescente: {vetor_crescente}')
