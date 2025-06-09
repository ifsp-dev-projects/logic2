
torres = {
    'A': [3, 2, 1],  
    'B': [],
    'C': []
}

NUM_DISCOS = len(torres['A'])
LARGURA_DISCO = 2 * NUM_DISCOS + 1 
def desenhar_torre():
    print("\nEstado atual das torres:\n")
    alturas = max(len(torre) for torre in torres.values())
    for nivel in range(alturas, 0, -1):
        linha = ""
        for haste in ['A', 'B', 'C']:
            torre = torres[haste]
            if len(torre) >= nivel:
                disco = torre[nivel - 1]
                largura = disco * 2 - 1
                espacos = (LARGURA_DISCO - largura) // 2
                linha += " " * espacos + "=" * largura + " " * espacos + "   "
            else:
                linha += " " * (LARGURA_DISCO // 2) + "|" + " " * (LARGURA_DISCO // 2) + "   "
        print(linha)
    print("   A" + " " * (LARGURA_DISCO - 1) + "   B" + " " * (LARGURA_DISCO - 1) + "   C\n")
    print("-" * 40)


def movimento_valido(origem, destino):
    if not torres[origem]:
        return False
    if not torres[destino]:
        return True
    return torres[origem][-1] < torres[destino][-1]

def jogo():
    print("=== Torre de Hanói ===")
    print("Objetivo: mover todos os discos da torre A para a torre C.")
    desenhar_torre()

    while torres['C'] != list(range(NUM_DISCOS, 0, -1)):
        origem = input("Mover de (A, B, C): ").strip().upper()
        destino = input("Mover para (A, B, C): ").strip().upper()

        if origem not in torres or destino not in torres:
            print("Haste inválida. Digite A, B ou C.")
            continue
        if origem == destino:
            print("Origem e destino são iguais. Tente novamente.")
            continue
        if movimento_valido(origem, destino):
            disco = torres[origem].pop()
            torres[destino].append(disco)
            desenhar_torre()
        else:
            print("Movimento inválido! Não pode colocar disco maior sobre menor.")

    print("Parabéns! Você completou a Torre de Hanói!")

jogo()
