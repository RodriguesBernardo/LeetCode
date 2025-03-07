palavras = ['amor', 'carinho', 'felicidade', 'alegria', 'tristeza', 'raiva', 'ódio', 'desprezo', 'amizade', 'solidão']


def procurar_palavra(palavra):
    for indice, p in enumerate(palavras):
        if p == palavra:
            return indice
        
print(procurar_palavra('alegria'))