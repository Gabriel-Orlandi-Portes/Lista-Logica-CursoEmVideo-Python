def Media(n1, n2):
    media = (n1 + n2) / 2
    return media


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = Media(nota1, nota2)
print('Média:', media)