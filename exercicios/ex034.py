altura = float(input('Digite sua altura em M: '))
peso = int(input('Digite seu peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'IMC:{imc} --> Abaixo do peso')
elif imc < 25:
    print(f'IMC:{imc} --> Peso ideal')
elif imc < 30:
    print(f'IMC:{imc} --> Sobrepeso')
elif imc < 40:
    print(f'IMC:{imc} --> Obesidade')
else:
    print(f'IMC:{imc} --> Obesidade mórbida')