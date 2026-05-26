qtde_alunos = 0
soma = 0

while True:
    idade = int(input('Digite a idade ou 999 para sair: '))

    if idade == 999:
        break

    qtde_alunos += 1
    soma += idade

if qtde_alunos > 0:
    media = soma / qtde_alunos

    print(f'Existem {qtde_alunos} alunos na turma.')
    print(f'A média de idade do grupo é {media:.2f} anos.')
else:
    print('Nenhum aluno foi informado.')