def Media(n1, n2):
    media = (n1 + n2) / 2
    return media


def Situacao(media):
    if media < 4:
        return 'REPROVADO'
    elif media < 7:
        return 'RECUPERAÇÃO'
    else:
        return 'APROVADO'


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = Media(nota1, nota2)
print('Média:', media)

situacao = Situacao(media)
print('Situação:', situacao)