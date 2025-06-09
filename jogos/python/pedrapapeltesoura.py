import random

print("Vamos jogar Pedra, Papel ou Tesoura!")
opcoes = ["pedra", "papel", "tesoura"]
pontuacaousuario = 0
pontuacaomaquina = 0

while pontuacaousuario < 5 and pontuacaomaquina < 5:
    numeroaleatorio = random.randint(0, 2)
    jogadaaleatoria = opcoes[numeroaleatorio]
    
    jogadausuario = input("Escolha entre Pedra, Papel ou Tesoura: ").lower()

    if jogadausuario not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue

    print(f"Computador escolheu: {jogadaaleatoria}")

    if jogadausuario == jogadaaleatoria:
        print("Empate!")
    elif (jogadausuario == "pedra" and jogadaaleatoria == "tesoura") or \
         (jogadausuario == "tesoura" and jogadaaleatoria == "papel") or \
         (jogadausuario == "papel" and jogadaaleatoria == "pedra"):
        print("Vitória!")
        pontuacaousuario += 1
    else:
        print("Derrota!")
        pontuacaomaquina += 1

    print(f"Placar: Você {pontuacaousuario} x {pontuacaomaquina} Computador\n")

if pontuacaousuario == 5:
    print("Parabéns! Você venceu.")
else:
    print("Que pena! Tente novamente.")
