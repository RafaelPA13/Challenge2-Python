from models.piloto import Piloto
from models.equipe import Equipe

# Numero de voltas que os carrinhos vao dar nas corridas
CORRIDA_NUMERO_DE_VOLTAS = 3
# Velocidade da corrida (quanto menor, mais rapido)
CORRIDA_VELOCIDADE = 0.5

EQUIPES = [
    Equipe("Porsche"),
    Equipe("Jaguar"),
    Equipe("MCLaren"),
    Equipe("Andretti"),
    Equipe("Nissan"),
    Equipe("Mahindra"),
    Equipe("Maseratti"),
]

CORES = {
    "BLACK": '\033[30m',
    "RED": '\033[31m',
    "GREEN": '\033[32m',
    "YELLOW": '\033[33m',
    "BLUE": '\033[34m',
    "MAGENTA": '\033[35m',
    "CYAN": '\033[36m',
    "WHITE": '\033[37m',
    "UNDERLINE": '\033[4m',
    "RESET": '\033[0m',
}

PILOTOS = [
    Piloto("Antonio Felix", EQUIPES[0], CORES["RED"]),
    Piloto("Nick Cassidy", EQUIPES[1], CORES["GREEN"]),
    Piloto("Oliver Rowland", EQUIPES[2], CORES["YELLOW"]),
    Piloto("Sam Bird", EQUIPES[3], CORES["BLUE"]),
    Piloto("Edoardo Mortara", EQUIPES[4], CORES["MAGENTA"]),
    Piloto("Maximilian Günther", EQUIPES[5], CORES["CYAN"]),
]
