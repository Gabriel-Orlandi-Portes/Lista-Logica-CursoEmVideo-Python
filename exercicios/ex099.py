def Potencia(base, expoente):
    potencia = base**expoente
    return potencia


n1 = int(input('Digite a base: '))
n2 = int(input('Digite o expoente: '))

potencia = Potencia(n1, n2)
print(potencia)