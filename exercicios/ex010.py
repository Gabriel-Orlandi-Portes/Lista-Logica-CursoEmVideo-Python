alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))  
area = alt * lar
tinta = area / 2   

print(f'A área da parede é de {area:.2f}m² e a quantidade de tinta necessária para pintá-la é de {tinta:.2f}L')