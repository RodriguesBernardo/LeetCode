import random as rd

def adivinha(x):
    numAleatorio = rd.randint(1, x)
    chute = 0 
    erros = 0
    while chute != numAleatorio:
        chute = int(input(f'Digite um número entre 1 e {x}: '))  
        if chute < numAleatorio:
            print("Desculpe, tente novamente. Muito baixo.")
            erros = erros + 1
        elif chute > numAleatorio:  
            print("Desculpe, tente novamente. Muito alto.")
            erros = erros + 1
    print(f'Parabéns, você adivinhou o número, {numAleatorio}, corretamente!!. Você cometeu {erros} erros.')

def computador_Adivinha(x):
    baixo = 1 
    alto = x
    resposta = ''
    while resposta != 'c': 
        if baixo != alto:
            palpite = rd.randint(baixo, alto)
        else:
            palpite = baixo 
        
        resposta = input(f'O número {palpite} é muito alto (A), muito baixo (B) ou correto (C)? ').lower()
        if resposta == 'a':  
            alto = palpite - 1
        elif resposta == 'b':  
            baixo = palpite + 1
    print(f'Parabéns! O computador adivinhou seu número, {palpite}, corretamente!')

computador_Adivinha(124)