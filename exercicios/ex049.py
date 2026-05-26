par = 0
impar = 0

for i in range(6):
    n1 = int(input('Digite um número: '))
    
    if n1 % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'A quantidade de números pares é {par} e a quantidade de ímpares é {impar}')