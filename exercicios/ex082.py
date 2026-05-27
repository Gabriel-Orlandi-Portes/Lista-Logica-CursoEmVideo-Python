notas = []
maiores_notas = []

acima_media = 0
soma = 0
maior_nota = 0 

for i in range(10):
    nota = float(input(f'Digite a nota do {i+1}º aluno: '))

    notas.append(nota)
    soma += nota

    if nota > maior_nota:
        maior_nota = nota
    
media = soma / 10

for n1 in notas:
    if n1 > media:
        acima_media += 1

for i in range(len(notas)):
    if notas[i] == maior_nota:
        maiores_notas.append(i)

print(f'A - A média da turma é {media:.2f}')
print(f'B - {acima_media} alunos estão acima da média')
print(f'C - A maior nota digitada foi {maior_nota}')
print(f'D - As maiores notas foram digitadas nas posições {maiores_notas}')