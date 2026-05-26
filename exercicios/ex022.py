from datetime import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade < 18:
    faltam = 18 - idade
    print(f'Faltam {faltam} anos para você se alistar no exército')
elif idade == 18:
    print('Você deve se alistar nesse ano')
else:
    passaram = idade - 18
    print(f'Já se passaram {passaram} anos que você se alistou no exército')