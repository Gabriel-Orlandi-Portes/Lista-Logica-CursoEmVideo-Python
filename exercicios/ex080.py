import random

vetor = []

for i in range(30):
    num = random.randint(1, 15)
    vetor.append(num)

n1 = int(input('Digite um número de 1 a 15: '))

posicao = []
qtde = 0

for i in range (len(vetor)):
    if vetor[i] == n1:
        posicao.append(i)
        qtde += 1

print(f' Chave escolhida: {n1} \n Posições no vetor em que a chave foi sorteada: {posicao} \n Quantidade de vezes que a chave foi sorteada: {qtde}')
