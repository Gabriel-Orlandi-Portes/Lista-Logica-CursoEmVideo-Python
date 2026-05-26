import random

sorteados = []
acima_de_5 = 0
div_3 = 0
for i in range(20):
    num = random.randint(0, 10)
    sorteados.append(num)

    if num > 5:
        acima_de_5 += 1
    
    if num % 3 == 0:
        div_3 += 1
print(f' A - Os numeros sorteados foram {sorteados} \n B - Quantidade de números maiores que 5: {acima_de_5} \n C - Quantidade de números divisíveis por por 3: {div_3}')