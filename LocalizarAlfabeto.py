alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def localizar_letras(nome):
    nome = nome.lower() 
    indices = []
    
    for letra in nome:
        if letra in alfabeto:  
            indices.append(alfabeto.index(letra))
    
    return indices

print(localizar_letras('Marcelo'))
