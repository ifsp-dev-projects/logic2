import random

tamanho = 7
navios = {
    'submarino': 3,
    'cruzador': 2,
    'bote': 1
}

agua = '~'
acerto = 'X'
erro = 'O'

oculto = [[agua for _ in range(tamanho)] for _ in range(tamanho)]
visivel = [[agua for _ in range(tamanho)] for _ in range(tamanho)]
info_navios = {}

def mostrar(tab):
    letras = 'ABCDEFG'
    print("  " + " ".join(str(i+1) for i in range(tamanho)))
    for i in range(tamanho):
        linha = " ".join(tab[i])
        print(letras[i], linha)

def pode_colocar(x, y, tam, direcao):
    if direcao == 'H':
        if y + tam > tamanho:
            return False
        return all(oculto[x][y+i] == agua for i in range(tam))
    else:
        if x + tam > tamanho:
            return False
        return all(oculto[x+i][y] == agua for i in range(tam))

def colocar_navios():
    for nome, tam in navios.items():
        colocado = False
        while not colocado:
            x = random.randint(0, tamanho - 1)
            y = random.randint(0, tamanho - 1)
            direcao = random.choice(['H', 'V'])
            if pode_colocar(x, y, tam, direcao):
                posicoes = []
                for i in range(tam):
                    xi = x + i if direcao == 'V' else x
                    yi = y + i if direcao == 'H' else y
                    oculto[xi][yi] = nome[0]  # usa a primeira letra
                    posicoes.append((xi, yi))
                info_navios[nome] = {
                    'tam': tam,
                    'pos': set(posicoes),
                    'acertos': set()
                }
                colocado = True

def valida(coord):
    if len(coord) < 2 or len(coord) > 3:
        return False
    linha = coord[0].upper()
    if linha not in 'ABCDEFG':
        return False
    try:
        col = int(coord[1:]) - 1
        if not (0 <= col < tamanho):
            return False
    except:
        return False
    return True

def jogo_acabou():
    return all(info['pos'] == info['acertos'] for info in info_navios.values())

print("=== BATALHA NAVAL (FÁCIL) ===")
print("Digite coordenadas como A1 até G7 para atirar.")
colocar_navios()

while not jogo_acabou():
    mostrar(visivel)
    tiro = input("Atirar em: ").strip().upper()

    if not valida(tiro):
        print("Entrada inválida.")
        continue

    lin = "ABCDEFG".index(tiro[0])
    col = int(tiro[1:]) - 1

    if visivel[lin][col] in (acerto, erro):
        print("Você já atirou aí.")
        continue

    alvo = oculto[lin][col]
    if alvo == agua:
        print("Água.")
        visivel[lin][col] = erro
    else:
        print("Acertou!")
        visivel[lin][col] = acerto
        for nome, dados in info_navios.items():
            if (lin, col) in dados['pos']:
                dados['acertos'].add((lin, col))
                if dados['acertos'] == dados['pos']:
                    print(f"Você afundou o {nome}!")
                break

print("\nVocê venceu! Todos os navios foram afundados.")
mostrar(visivel)
