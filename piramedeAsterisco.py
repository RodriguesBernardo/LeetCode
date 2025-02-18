def piramede(tamanho):
    for i in range(1, tamanho + 1):
        print(" " * (tamanho - i) + "*" * (2 * i - 1))
        
        
piramede(1)