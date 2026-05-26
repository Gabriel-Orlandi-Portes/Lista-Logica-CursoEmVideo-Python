import random

n1 = int(input('Digite um número de 1 a 5: '))
num = random.randint(1,5)

if n1 == num: 
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez!')