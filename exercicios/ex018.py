from datetime import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade < 16:
    print('Você não pode votar')
elif idade < 18:
    print('Voto opcional')
elif idade < 70:
    print('Voto obrigatório')
else:
    print('Voto opcional')