def retornarPares(inicio:int, fim:int) -> list:
    lista = []
    for i in range(inicio, fim +1 ):
        lista.append(i)
    
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)  
    return pares  



print(retornarPares(1, 20))
