import time

from betting.apostas.melhorEquipe import ApostaMelhorEquipe
from betting.apostas.melhorVolta import ApostaMelhorVolta
from betting.apostas.tresPrimeirosColocados import ApostaTop3
from betting.gerenciadorDeApostas import BettingSystem
from configs import PILOTOS, EQUIPES, CORRIDA_VELOCIDADE, CORRIDA_NUMERO_DE_VOLTAS
from partida import Game
from utils.terminal import limpar_terminal

limpar_terminal()

game = Game(PILOTOS, EQUIPES, CORRIDA_VELOCIDADE, CORRIDA_NUMERO_DE_VOLTAS)

apostas_disponiveis = [ApostaTop3(10), ApostaMelhorEquipe(30), ApostaMelhorVolta(30)]
bettingSystem = BettingSystem(apostas_disponiveis, PILOTOS, EQUIPES)
bettingSystem.coletar_apostas()

print("A corrida começará em...")
seconds = 3
while seconds > 0:
    print(f"{seconds}...")
    seconds -= 1
    time.sleep(1)

resultado = game.iniciar_corrida()
bettingSystem.avaliar_apostas(resultado)
