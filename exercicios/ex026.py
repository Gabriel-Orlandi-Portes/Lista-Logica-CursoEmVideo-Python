n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior do que o segundo valor ({n2})')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior do que o primeiro valor ({n1})')
else:
    print('Os números são iguais!')