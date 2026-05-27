def Fibonacci(qtde_termos):
    n1 = 1
    n2 = 1

    for i in range(qtde_termos):
        print(n1, end = ' >> ')

        n3 = n2 + n1
        n1 = n2
        n2 = n3
    print('FIM')

termo = int(input('Digite o termo para a sequência de fibonacci: '))

Fibonacci(termo)
