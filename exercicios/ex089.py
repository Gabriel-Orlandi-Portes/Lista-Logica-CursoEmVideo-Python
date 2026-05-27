def Gerador(texto, qtde, borda):
    
    if borda == 1:
        linha = '+-------=======------+'
    elif borda == 2:
        linha = '~~~~~~~~:::::::~~~~~~~'
    elif borda == 3:
        linha = '<<<<<<<<------->>>>>>>'
    
    print(linha)
    
    for i in range(qtde):
        print(texto)
    
    print(linha)

Gerador('Portugol studio', 3, 2)