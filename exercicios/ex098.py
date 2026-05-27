def SuperSomador(inicio, fim):
    soma = 0
    for i in range(inicio, fim+1, 1):
        soma += i
    return soma

n1 = int(input('Digite o início: '))
n2 = int(input('Digite o fim: '))

soma = SuperSomador(n1, n2)
print(soma)


