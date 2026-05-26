import random

num = random.randint(1, 10)
i = 0

while i < 4:
    n1 = int(input(f'{i+1}ª Tentativa - Digite um número de 1 a 10: '))

    if n1 == num:
        print('Parabéns, você acertou!')
        break
    else:
        print('Não foi dessa vez!')

    i += 1