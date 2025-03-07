primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))   
terceiraNota = float(input("Digite a terceira nota: ")) 

media = (primeiraNota + segundaNota + terceiraNota) / 3

if media >= 7:
    print("Parabens você foi aprovado com média: ", media.__round__(1))  
else: 
    print("Você foi reprovado com média: ", media)  
    
