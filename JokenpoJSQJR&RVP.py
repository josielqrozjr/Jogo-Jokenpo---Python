import random

def jogadaInvalida():
    mode = 0
    while mode > 3 or mode < 1:
        mode = int(input("Digite um número para o modo de jogo:"  # Comando que determina a modalidade do jogo.
                         "\n1 - Jogador X Jogador"
                         "\n2 - Jogador X Computador"
                         "\n3 - Computador X Computador \n>>> "))
    return mode

def jogadaValidaHumano(id):
    jogada = 0
    while jogada < 1 or jogada > 3:
        jogada = int(input("Jogador " + id + "  [1 - Pedra | 2 - Papel | 3 - Tesoura] >>> "))
    return jogada


def jogadaValidaComputador(id):
    jogada = random.randint(1, 3)
    print("Jogador " + id + "  [1 - Pedra | 2 - Papel | 3 - Tesoura] >>> {}".format(jogada))
    return jogada


start = "SIM"
move = 0  # Pontuação da rodada
scoreOne = 0  # Pontuação do jogador 1
scoreTwo = 0  # Pontuação do jogador 2
purple = '\033[7;35m'  # Personalização
clean = '\033[m'  # Limite da cor
cyan = '\033[7;36m'  # Personalização
yellow = '\033[7;43m'  # Personalização

print("{} Bem-vindo ao ---> JOKENPÔ <--- {}".format(purple, clean))
mode = int(input("Digite um número para o modo de jogo:"  # Comando que determina a modalidade do jogo.
                 "\n1 - Jogador X Jogador"
                 "\n2 - Jogador X Computador"
                 "\n3 - Computador X Computador \n>>> "))

while start == "SIM":  # Comando responsável pela continuação das rodadas.
    move += 1
    print(">>> {} RODADA {} {} <<<".format(purple, move, clean))
    playerOne = -1
    playerTwo = -1

    if mode == 1:
        playerOne = jogadaValidaHumano("1")
        playerTwo = jogadaValidaHumano("2")
    elif mode == 2:
        playerOne = jogadaValidaHumano("1")
        playerTwo = jogadaValidaComputador("2")
    elif mode == 3:
        playerTwo = jogadaValidaComputador("1")
        playerTwo = jogadaValidaComputador("2")

    else:
        print("Modalidade inexistente")
        mode = jogadaInvalida()



    if playerOne == 1 and playerTwo == 3 \
            or playerOne == 2 and playerTwo == 1 \
            or playerOne == 3 and playerTwo == 2:  # Condições para a vitória do jogador 1
        scoreOne += 1
    elif playerTwo == 1 and playerOne == 3 \
            or playerTwo == 2 and playerOne == 1 \
            or playerTwo == 3 and playerOne == 2:  # Condições para a vitória do jogador 2
        scoreTwo += 1
    else:
        print("EMPATE!")
        scoreOne += 1
        scoreTwo += 1

    start = str(input("Jogar novamente: [SIM] [NÃO] ")).upper()

print("PLACAR: [Jogador 01] {} {} {}  |  [Jogador 02] {} {} {}".format(cyan, scoreOne, clean, yellow, scoreTwo, clean))
print("Thank you for player! \nDevelopers >>> Josiel Queiroz, Jr. and Rafaela Vecchi Pelentier <<<")