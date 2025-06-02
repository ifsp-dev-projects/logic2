import random
print("O tema da rodada é: desenhos animados")
palavras=["O incrível mundo de Gumball", "Winx", "Bob Esponja", "Jovens Titãs", "Hora de Aventura" ]
numeroaleatorio=random.randint(0,4)
palavradaforca=palavras[numeroaleatorio].lower()
tentativas=[]
erros=0
while erros<=6:
    letra=(input("Digite uma letra :")).lower()
    if letra in palavradaforca:
        print("Letra correta!")
    else:
        print("Letra errada!")
        erros += 1
        
    if letra not in tentativas:
        tentativas.append(letra)
        
    resultado = "".join(c if c in tentativas or c == " " else "_" for c in palavradaforca)
    print(resultado)

    if "_" not in resultado:  
        print("Parabéns! Você acertou a palavra!")
        break
    
if erros>6:
    print("Você excedeu o número máximo de tentativas! Tente novamente.")