import random

opcoes = ['pedra', 'papel', 'tesoura']

computador = random.choice(opcoes)

jogador = input("Pedra, papel ou tesoura: ").lower()

print(f"Computador escolheu: {computador}")

if jogador not in opcoes:
    print("Jogada inválida! Tente novamente.")
elif jogador == computador:
    print("Empate!")
elif (
    (jogador == 'pedra' and computador == 'tesoura') or
    (jogador == 'papel' and computador == 'pedra') or
    (jogador == 'tesoura' and computador == 'papel')
):
    print("Você ganhou!")
else:
    print("Você perdeu!")